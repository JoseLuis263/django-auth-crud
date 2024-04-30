from django import forms
from .models import Activities

class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['image','video_link', 'description']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a description'})
            
        }
