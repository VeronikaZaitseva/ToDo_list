from django import forms
from .models import Task


class TodoForm(forms.ModelForm):
    title = forms.CharField(label='Name')
    content = forms.CharField(label='Content', widget=forms.widgets.Textarea())
    priority = forms.ChoiceField(label='Priority', widget=forms.widgets.Select(), choices=Task.colors)

    class Meta:
        model = Task
        fields = ['title', 'content', 'priority']
