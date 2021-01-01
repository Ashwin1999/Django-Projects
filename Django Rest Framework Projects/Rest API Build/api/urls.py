from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview, name="api-overview"),
    path('task-list/', taskList, name="task-list"),
    path('task-detailed/<int:pk>/', taskDetailed, name="task-detailed"),
    path('task-create/', taskCreate, name="task-create"),
    path('task-update/<int:pk>/', taskUpdate, name="task-update"),
    path('task-delete/<int:pk>/', taskDelete, name="task-delete"),
]