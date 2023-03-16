from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(ModelForm):
    # scrisul din titlul de la search bar
    titlu = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Adauga un nou task...'}))

    class Meta:
        model = Task
        fields = '__all__'
