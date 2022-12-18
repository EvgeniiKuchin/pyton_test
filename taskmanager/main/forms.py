from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["task", "title"]
        widgets = {"task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите Описание'}), "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),}
