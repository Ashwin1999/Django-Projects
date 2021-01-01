from django.shortcuts import render
from .models import PersonalBlog


# Create your views here.
def home(request):
    context = {}
    return render(request, 'myApp/home.html', context=context)
