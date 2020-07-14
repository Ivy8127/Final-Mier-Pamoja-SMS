from django.db import models
from academic.models import Department
from administration.models import Designation

# Create your models here.
class JobInfo(models.Model):
    category_choice =(
        ('Government','Government'),
        ('Non-Government','Non-Government')
    )
    category = models.CharField(choices= category_choice , max_length =50)
    joining_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length = 100)
    job_designation = models.ForeignKey(Designation ,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.department)
    class Meta():
        verbose_name_plural = 'Job Information'


class TrainingInfo(models.Model):
    """Information about where a teacher trained at

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    institution_name = models.CharField(max_length = 100)
    year = models.IntegerField()
    duration = models.IntegerField()
    location = models.CharField(max_length = 100)

    def __str__(self):
        return self.institution_name
    class Meta():
        verbose_name_plural = 'Training Information'


class ExperienceInfo(models.Model):
    """Provides info on the experience of a particular teacher(TP)

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    institute_name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 50)
    trainer = models.CharField(max_length = 50)
    def __str__(self):
        return self.institute_name
    class Meta():
        verbose_name_plural ='Experience Information'    

class PersonalInfo(models.Model):
    name = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to = 'teacher_photos/',blank = True)
    date_of_birth = models.DateField()
    gender_status = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
        
    )
    gender = models.CharField(max_length = 50,choices = gender_status)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField(blank = True)
    father_name = models.CharField(max_length = 50)
    mother_name = models.CharField(max_length = 50)
    religion_status = (
        ('Christian','Christian'),
        ('Muslim','Muslim'),
        ('Other','Other')
    )
    religion = models.CharField(max_length =50 ,choices = religion_status)
    marital_status_choice =(
        ('Married','Married'),
        ('Widowed','Widowed'),
        ('Separated','Separated'),
        ('Divorced','Divorced'),
        ('Single','Single')

    )
    marital_status = models.CharField(choices = marital_status_choice,max_length=10)
    experience = models.ForeignKey(ExperienceInfo, on_delete=models.CASCADE ,null = True,blank = True)
    training = models.ForeignKey(TrainingInfo, on_delete=models.CASCADE , null = True)
    job = models.ForeignKey(JobInfo ,on_delete=models.CASCADE , null = True)
    date = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        
        """Rerutn a string representation of a teacher's name

        Returns:
            [type] -- [description]
        """
        return self.name

    class Meta:
        verbose_name_plural = 'Personal Information'


