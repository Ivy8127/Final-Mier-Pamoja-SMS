from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AdminLoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Username'}))

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']   

