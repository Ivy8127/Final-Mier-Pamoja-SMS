from django.shortcuts import render
from django.http import HttpResponse
from student.models import AcademicInfo
from teacher.models import PersonalInfo
from academic.models import ClassRegistration
from parent.models import Personalinfo

def home_page(request):
    total_student = AcademicInfo.objects.count()
    total_teacher = PersonalInfo.objects.count()
    total_class = ClassRegistration.objects.count()
    total_parent = Personalinfo.objects.count()
    context={
        'student': total_student,
        'teacher': total_teacher,
        'academic': total_class,
        'parent': total_parent,
    }
    return render(request, 'home.html',context)
    