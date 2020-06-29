from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from academic.models import ClassInfo
from .forms import *

# Create your views here.

def student_registration(request):
    personal_info_form = PersonalInfoForm(request.POST)
    academic_info_form = AcademicInfoForm(request.POST)


    if request.method == 'POST':

        if personal_info_form.is_valid() and academic_info_form.is_valid():
            s1=personal_info_form.save()
            s2=academic_info_form.save()
            academic_info = academic_info_form.save(commit=False)
            academic_info.personalInfo = s1
            academic_info.save()

            return redirect('student:student-list')

    context ={
        'personal_info_form':personal_info_form,
        'academic_info_form':academic_info_form
    }
    
    return render(request , 'student/student_registration.html',context)

#def student_profile(request):
    #return HttpResponse("student profile page")

def student_list(request):
    """Shows the whole list of students

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    students = AcademicInfo.objects.all()
    context ={'students':students }
    return render(request,'student/student_list.html',context)


def student(request,student_id):
    student = PersonalInfo.objects.get(id=student_id)
    context = {'student':student}
    return render(request,'student/student.html',context)
    
#def student_edit(request):
    #return HttpResponse("student edit page")

#def student_delete(request):
   # return HttpResponse("student delete page")

def enrolled_student(request):
    return render(request ,'student/enrolled.html')

#def student_enrolled(request):
    #return HttpResponse("student enrolled page")

def enrolled_student_list(request):
    return render(request,'student/enrolled_student_list.html')