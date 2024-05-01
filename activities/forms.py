from django import forms
from .models import Activities

class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['description', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a description'})
            
        }
