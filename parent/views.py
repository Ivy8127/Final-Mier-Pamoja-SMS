# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def parent_registration(request):
    """A parent registration form that is sent back to the database when it is valid

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    personal_info_form = ParentPersonalInfoForm(request.POST)
    

    if request.method == 'POST':

        if personal_info_form.is_valid():
            personal_info_form.save()
            return redirect('parent:parent-list')

    context ={
        'personal_info_form':personal_info_form,
    }
    
    return render(request, 'parent/parent_registration.html',context)

def parent_profile(request,parent_name):
    """Returns a student to their profile page

    Args:
        request ([type]): [description]
        reg_no ([type]): [description]

    Returns:
        [type]: [description]
    """
    parent = Personalinfo.objects.get(name = parent_name)
    context = {'parent':parent}
    return render(request,'parent/parent-profile.html',context)



def parent_list(request):
    """Shows the whole list of parents

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    parents =Personalinfo.objects.filter(is_delete=False).order_by('-id')
    context ={'parents' : parents }
    return render(request,'parent/parent_list.html',context)



def parent_edit(request,parent_name):
    """Edit's the parent registration form and redirects them to the parent list page

    Args:
        request ([type]): [description]
        reg_no ([type]): [description]

    Returns:
        [type]: [description]
    """
#GET METHOD = BLANK FORM
    parent = Personalinfo.objects.get(name=parent_name)
    personal_info_form = ParentPersonalInfoForm(instance=parent)
    
#POST METHOD = FILL IT WITH DATA
    if request.method == 'POST':
        personal_info_form = ParentPersonalInfoForm(request.POST,instance=parent)
        

        if personal_info_form.is_valid():
            s1=personal_info_form.save()

            return redirect('parent:parent-list')
            
    context ={
        'personal_info_form':personal_info_form,
    }
    
    return render(request,'parent/parent-edit.html',context)




def parent_delete(request,parent_name):
    """Deletes a parent

    Args:
        request ([type]): [description]
        reg_no ([type]): [description]

    Returns:
        [type]: [description]
    """
    parent = Personalinfo.objects.get(name = parent_name)
    parent.is_delete = True
    parent.save()
    return redirect('parent:parent-list')







