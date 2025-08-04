from django import forms
from .models import Todo
from django_summernote.widgets import SummernoteWidget

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'content', 'image']
        widgets = {
            'content': SummernoteWidget(),
        }
