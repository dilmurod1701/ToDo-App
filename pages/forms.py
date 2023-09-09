from django import forms

from .models import tasks


class Tasks(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['title', 'description', 'start', 'finish']
        widgets = {
            'start': forms.DateInput({'type': 'date'}),
            'finish': forms.DateInput({'type': 'date'}),
        }
