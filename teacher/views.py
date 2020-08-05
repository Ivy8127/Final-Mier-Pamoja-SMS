from django.shortcuts import render, redirect
from . import forms
from . models import *




def teacher_registration(request):
    form = forms.PersonalInfoForm()
    training_form = forms.TrainingInfoForm()
    job_form = forms.JobInfoForm()
    experience_form = forms.ExperienceInfoForm()
    if request.method == 'POST':
        form = forms.PersonalInfoForm(request.POST, request.FILES)
        training_form = forms.TrainingInfoForm(request.POST)
        job_form = forms.JobInfoForm(request.POST)
        experience_form = forms.ExperienceInfoForm(request.POST)
        if form.is_valid() and training_form.is_valid() and job_form.is_valid() and experience_form.is_valid():
            training_info = training_form.save()
            job_info = job_form.save()
            experience_info = experience_form.save()
            personal_info = form.save(commit=False)
            personal_info.training = training_info
            personal_info.job = job_info
            personal_info.experience = experience_info
            personal_info.save()
            return redirect('teacher:teacher-list')

    context = {
        'form': form,
        'training_form': training_form,
        'job_form': job_form,
        'experience_form': experience_form
    }
    return render(request, 'teacher/teacher-registration.html', context)




def teacher_list(request):
    teacher = PersonalInfo.objects.all()
    context = {'teacher': teacher}
    return render(request, 'teacher/teacher-list.html', context)


def teacher_profile(request, teacher_id):
    teacher = PersonalInfo.objects.get(id=teacher_id)
    context = {
        'teacher': teacher
    }
    return render(request, 'teacher/teacher-profile.html', context)



def teacher_delete(request, teacher_id):
    teacher = PersonalInfo.objects.get(id=teacher_id)
    teacher.is_delete = True
    teacher.save()
    return redirect('teacher:teacher-list')



def teacher_edit(request, teacher_id):
    teacher = PersonalInfo.objects.get(id=teacher_id)
    form = forms.PersonalInfoForm(instance=teacher)
    training_form = forms.TrainingInfoForm(instance=teacher.training)
    job_form = forms.JobInfoForm(instance=teacher.job)
    experience_form = forms.ExperienceInfoForm(instance=teacher.experience)
    if request.method == 'POST':
        form = forms.PersonalInfoForm(request.POST, request.FILES, instance=teacher)
        training_form = forms.TrainingInfoForm(request.POST, instance=teacher.training)
        job_form = forms.JobInfoForm(request.POST, instance=teacher.job)
        experience_form = forms.ExperienceInfoForm(request.POST, instance=teacher.experience)
        if form.is_valid() and training_form.is_valid() and job_form.is_valid() and experience_form.is_valid():
            training_info = training_form.save()
            job_info = job_form.save()
            experience_info = experience_form.save()
            personal_info = form.save(commit=False)
            personal_info.training = training_info
            personal_info.job = job_info
            personal_info.experience = experience_info
            personal_info.save()
            return redirect('teacher:teacher-list')
    context = {
        'form': form,
        'training_form': training_form,
        'job_form': job_form,
        'experience_form': experience_form
    }
    return render(request, 'teacher/teacher-edit.html', context)
    