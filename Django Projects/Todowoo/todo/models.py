from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class todolist(models.Model):
    title = models.CharField(max_length=100)
    todo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    finish = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
