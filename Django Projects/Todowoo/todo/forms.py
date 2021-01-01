from django.forms import ModelForm
from .models import todolist
from django import forms


class TodoForm(ModelForm):
    class Meta:
        model = todolist
        fields = ['title', 'todo', 'important']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'todo': forms.Textarea(attrs={'class': 'form-control'}),
            'important': forms.CheckboxInput(),
        }
