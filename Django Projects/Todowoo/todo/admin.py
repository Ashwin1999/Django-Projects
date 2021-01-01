from django.contrib import admin
from .models import todolist

# Register your models here.


class todoadmin(admin.ModelAdmin):
    readonly_fields = ['created']


admin.site.register(todolist, todoadmin)
