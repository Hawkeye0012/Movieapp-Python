from django import forms
from .models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies  # Table name
        fields = ['name', 'description', 'img', 'year']  # Fields we want to edit
