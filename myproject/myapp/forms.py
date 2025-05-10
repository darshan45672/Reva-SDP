from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List

        fields = ['title', 'description', 'is_done']

        widgets ={
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'is_done' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }