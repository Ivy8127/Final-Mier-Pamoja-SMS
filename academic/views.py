from django.shortcuts import render,redirect
from .models import *
from .forms import ClassForm,ClassRegistrationForm
from . import forms




def add_class(request):
    forms = ClassForm()
    if request.method == 'POST':
        forms = ClassForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('academic:create-class')
    class_object = ClassInfo.objects.all()        

    context = {
        'forms': forms,
        'class_object' : class_object
    }        

    return render(request ,'academic/create-class.html',context)        





def class_list(request):
    class_register = ClassRegistration.objects.all()
    context = {
        'class_register': class_register,
    }
    return render(request , 'academic/class-list.html',context)



def class_registration(request):
    forms = ClassRegistrationForm()
    if request.method == 'POST':
        forms = ClassRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('academic:class-list')
    context = {
        'forms': forms
    }
    return render(request ,'academic/class-registration.html',context)


