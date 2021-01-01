from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        chars.extend([x.upper() for x in chars])
    if request.GET.get('numbers'):
        chars.extend(list(
            '0123456789'))
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*-_<>.~`'))
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return render(request, 'generator/password.html', {'password': password})
