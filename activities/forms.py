from django import forms
from .models import Activities

class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['imagen', 'description']
        widgets = {
            'imagen': forms.FileInput(attrs = {"id" : "image_field"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a description'})
            
        }
