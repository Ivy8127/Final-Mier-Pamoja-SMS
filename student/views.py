from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from academic.models import ClassInfo
from .forms import *

# Create your views here.

def student_registration(request):
    """A student registration form that is sent back to the database when it is valid

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
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

def student_profile(request,reg_no):
    """Returns a student to their profile page

    Args:
        request ([type]): [description]
        reg_no ([type]): [description]

    Returns:
        [type]: [description]
    """
    student = AcademicInfo.objects.get(registration_no = reg_no)
    context = {'student':student}
    return render(request,'student/student-profile.html',context)



def student_list(request):
    """Shows the whole list of students

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    students = AcademicInfo.objects.filter(is_delete=False).order_by('-id')
    context ={'students':students }
    return render(request,'student/student_list.html',context)




def student(request,student_id):
    student = PersonalInfo.objects.get(id=student_id)
    context = {'student':student}
    return render(request,'student/student.html',context)



def student_edit(request,reg_no):
    """Edit's the student registration form and redirects them to the student list page

    Args:
        request ([type]): [description]
        reg_no ([type]): [description]

    Returns:
        [type]: [description]
    """
#GET METHOD = BLANK FORM
    student = AcademicInfo.objects.get(registration_no=reg_no)
    personal_info_form = PersonalInfoForm(instance=student.personalInfo)
    academic_info_form = AcademicInfoForm(instance=student)

#POST METHOD = FILL IT WITH DATA
    if request.method == 'POST':
        personal_info_form = PersonalInfoForm(request.POST,instance=student.personalInfo)
        academic_info_form = AcademicInfoForm(request.POST,instance=student)

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
    
    return render(request,'student/student-edit.html',context)




def student_delete(request,reg_no):
    """Deletes a student 

    Args:
        request ([type]): [description]
        reg_no ([type]): [description]

    Returns:
        [type]: [description]
    """
    student = AcademicInfo.objects.get(registration_no = reg_no)
    student.is_delete = True
    student.save()
    return redirect('student:student-list')



def enrolled_student(request):
    forms = EnrolledStudentForm()
    class_name =request.GET.get('class_name',None)
    student = AcademicInfo.objects.filter(class_info = class_name, status='not enrolled')
    context = {
        'forms': forms,
        'student':student,
    }
    
    return render(request,'student/enrolled.html',context)



def student_enrolled(request, reg):
    """Enrolls a student into the system trough a StudentEnrollForm

    Args:
        request ([type]): [description]
        reg_no ([type]): [description]

    Returns:
        [type]: [description]
    """
    student = AcademicInfo.objects.get(registration_no = reg)
    forms = StudentEnrollForm()
    if request.method == 'POST':
        forms = StudentEnrollForm(request.POST)
        if forms.is_valid():
            roll = forms.cleaned_data['roll_no']
            class_name =forms.cleaned_data['class_name']
            EnrolledStudent.objects.create(class_name=class_name,student=student,roll=roll)
            student.status = 'enrolled'
            student.save()
            return redirect('student:enrolled-student-list')

    context = {
       
        'student':student,
         'forms': forms
    }
    return render(request,'student/student-enrolled.html',context)





def enrolled_student_list(request):
    student = EnrolledStudent.objects.all()
    forms = SearchEnrolledStudentForm()
    class_name = request.GET.get('reg_class',None)
    roll = request.GET.get('roll_no',None)
    if class_name:
        student = EnrolledStudent.objects.filter(class_name=class_name)
        context = {
            'forms': forms,
            'student': student
        }
        return render(request, 'student/enrolled-student-list.html',context)
    context ={
        'forms':forms,
        'student': student
    }

    return render(request,'student/enrolled-student-list.html',context)