from django import forms
from .models import *




class ParentPersonalInfoForm(forms.ModelForm):
    class Meta:
        model = Personalinfo
        exclude =['is_delete']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'photo' : forms.ClearableFileInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'phone_no' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'religion' : forms.Select(attrs={'class':'form-control'}),
            'relationship_to_student' : forms.Select(attrs={'class':'form-control'}),
            'parent_to': forms.TextInput(attrs={'class':'form-control'}),

        }

