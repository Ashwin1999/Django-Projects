from .views import *
from django.urls import path

urlpatterns = [
    path('', Overview, name='Overview'),
    path('get-post/<int:pk>/', GetPost, name='GetPost'),
    path('get-post/', GetPosts, name='GetPosts'),
    path('post-post/', PostPost, name='PostPost'),
    path('put-post/<int:pk>/', PutPost, name='PutPost'),
    path('delete-post/<int:pk>/', DeletePost, name='DeletePost')
]
