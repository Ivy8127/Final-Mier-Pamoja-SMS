from django import forms
from .models import *
from academic.models import ClassInfo



class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'photo' : forms.ClearableFileInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'phone_no' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'religion' : forms.Select(attrs={'class':'form-control'}),
            'birth_certficate_no' : forms.TextInput(attrs={'class':'form-control'}),

        }

class AcademicInfoForm(forms.ModelForm):
    class Meta:
        model = AcademicInfo
        exclude = ['date','personalInfo','status','is_in_session']
        widgets = {
            'class_info': forms.Select(attrs={'class':'form-control'}),
            'registration_no': forms.NumberInput(attrs={'class':'form-control'}),
            'is_in_session': forms.CheckboxInput(attrs={'class':'form-control'}),
        }

class EnrolledStudentForm(forms.ModelForm):
    model = EnrolledStudent
    fields = ['__all__']
    widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'class_name' : forms.TextInput(attrs={'class':'form-control'}),
            'student_registration_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
            'date' : forms.SelectDateWidget(attrs={'class':'form-control'}),

        }
    

class StudentEnrollForm(forms.Form):
    class_name = forms.ModelChoiceField(queryset=ClassRegistration.objects.all())
    student_registration_no = forms.IntegerField(widget = forms.NumberInput(attrs={'class':'form-control'}))
        