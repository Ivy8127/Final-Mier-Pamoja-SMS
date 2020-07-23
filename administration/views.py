from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages



def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"Username OR password is incorrect")
                return render(request, 'administration/login.html')

    context = {
        'forms':forms
    }
    return render(request, 'administration/login.html',context)

def admin_logout(request):
    logout(request)
    return redirect('login')

def admin_register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user)
            return redirect('login')


    context={'form':form}  
    return render(request,'administration/register.html',context)           
