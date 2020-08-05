from django import forms
from . import models
from academic.models import ClassInfo,ClassRegistration



class ClassForm(forms.ModelForm):
    class Meta:
        model = models.ClassInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'display_name': forms.TextInput(attrs={'class':'form-control'}),
            
        }


class ClassRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.ClassRegistration
        exclude = ['date']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'classinfo': forms.Select(attrs={'class':'form-control'}),
        }
