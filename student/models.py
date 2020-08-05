from django.db import models
import random

from academic.models import ClassInfo ,ClassRegistration


# Create your models here.
class PersonalInfo(models.Model):
    """Returns the personal information about a student

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    name = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to = 'student-photos/',blank = True ,null=True)
    date_of_birth = models.DateField()
    gender_choices =(
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
        
    )
    gender = models.CharField(choices = gender_choices,max_length=10)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField(blank = True)
    religion_choice =(
        ('christian','Christian'),
        ('muslim','Muslim'),
        ('other','Other'),
    )
    religion = models.CharField(choices = religion_choice,max_length = 50)
    birth_certificate_no = models.IntegerField(default=000000)

    def __str__(self):
        
        """Return a string representation of a student's name

        Returns:
            [type] -- [description]
        """
        return self.name
    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo ,'url'):
            return self.photo.url    
       

    class Meta:
        verbose_name_plural = 'Personal Information'


class AcademicInfo(models.Model):
    """Provides the academic information about a student

    Arguments:
        models {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    class_info = models.ForeignKey(ClassInfo , on_delete=models.CASCADE)
    registration_no = models.IntegerField(unique=True,default = random.randint(000000,999999))
    personalInfo = models.ForeignKey(PersonalInfo, on_delete= models.CASCADE ,null = True,max_length =6)
    is_delete = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    status_select =(
        ('enrolled','Enrolled'),
        ('not enrolled','Not Enrolled')
    )
    status = models.CharField(max_length = 20 ,choices = status_select, default ='Not Enrolled')

    def __str__(self):
        """Returns a student's academic info
        Returns:
            [type] -- [description]
        """
        return str(self.registration_no)

    class Meta():
        verbose_name_plural = 'Academic Information'

class EnrolledStudent(models.Model):
    """Shows a list of all the enrolled students in the system

    Arguments:
        models {[type]} -- [description]
    """
    class_name = models.ForeignKey(ClassRegistration,on_delete=models.CASCADE)
    student = models.OneToOneField(AcademicInfo,on_delete=models.CASCADE)
    roll = models.IntegerField(default = 000000)
    date = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = ['class_name','roll']
    
    def __str__(self):
        return str(self.roll)
    