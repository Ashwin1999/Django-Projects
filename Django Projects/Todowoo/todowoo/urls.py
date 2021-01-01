from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('', views.home, name='home'),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    # Todos
    path('todos/', views.todos, name='todos'),
    path('yourtodos/', views.listtodos, name='listtodos'),
    # view or update todos
    path('todo/<int:todo_pk>', views.detailview, name='detailview'),
    # complete or delete todos
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
    # view completed todos
    path('complete/', views.viewcomplete, name='viewcomplete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
