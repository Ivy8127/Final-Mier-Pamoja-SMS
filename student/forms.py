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
        exclude = ['date','personalInfo','status','is_delete']
        widgets = {
            'class_info': forms.Select(attrs={'class':'form-control'}),
            
        }

class EnrolledStudentForm(forms.Form):
    class_name = forms.ModelChoiceField(queryset=ClassInfo.objects.all())




class StudentEnrollForm(forms.Form):
    class_name = forms.ModelChoiceField(queryset=ClassRegistration.objects.all())
    roll_no = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter roll','class':'form-control'}))


class SearchEnrolledStudentForm(forms.Form):
    reg_class = forms.ModelChoiceField(queryset=ClassRegistration.objects.all())
    roll_no = forms.IntegerField(required= False,widget=forms.NumberInput(attrs={'placeholder':'Enter Roll:'}))    