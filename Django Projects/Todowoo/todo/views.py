from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# import user creation form and login form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# import built in user model
from django.contrib.auth.models import User
# import IntegrityError
from django.db import IntegrityError
# import logout
from django.contrib.auth import logout, authenticate, login
# use decorator login required to give access to page only if user is logged in
from django.contrib.auth.decorators import login_required
# use TodoForm from forms.py
from .forms import TodoForm
# get todo model to list it out in an HTML format
from .models import todolist

# timezone needed for complete/finish functionality
from django.utils import timezone

# Create your views here.


def signupuser(request):
    # if the request method is get, you need to render the page. otherwise, someone is submitting the form.
    # do what is necessary
    if request.method == "GET":
        return render(request, 'todo/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('loginuser')
            except IntegrityError:
                return render(request, 'todo/signup.html', {'form': UserCreationForm(), 'error': 'Username Already exists. Please choose a new Username'})
        else:
            # print("You've entered a different password!")
            return render(request, 'todo/signup.html', {'form': UserCreationForm(), 'error': 'passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/login.html', {'form': AuthenticationForm(), 'error': 'User does not exist'})
        else:
            login(request, user)
            return redirect('home')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('loginuser')


def home(request):
    return render(request, 'todo/home.html')


@login_required
def todos(request):
    if request.method == 'GET':
        return render(request, 'todo/todolist.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('home')
        except ValueError:
            return render(request, 'todo/todolist.html', {'form': TodoForm(), 'error': 'title is too long. limit it to 100 words'})


@login_required
def listtodos(request):
    todo = todolist.objects.filter(user=request.user, finish__isnull=True)
    return render(request, 'todo/listtodos.html', {'todos': todo})


@login_required
def detailview(request, todo_pk):
    todo = get_object_or_404(todolist, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/detailview.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect(listtodos)
        except ValueError:
            return render(request, 'todo/detailview.html', {'todo': todo, 'form': form, 'error': 'ValueError'})


@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(todolist, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.finish = timezone.now()
        todo.save()
        return redirect(listtodos)


@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(todolist, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect(listtodos)


@login_required
def viewcomplete(request):
    todo = todolist.objects.filter(user=request.user, finish__isnull=False)
    return render(request, 'todo/viewcomplete.html', {'todos': todo})
