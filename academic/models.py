from django.db import models
from django.contrib.auth.models import User





# Create your models here.
class ClassInfo(models.Model):
    """Provides the basic information about a class

    Arguments:
        models {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    name = models.CharField(max_length =50,unique = True)
    display_name = models.CharField(max_length = 15, unique = True)
    date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        """Returns the name of a class

        Returns:
            [type] -- [description]
        """
        return self.name
    class Meta():
        verbose_name_plural = 'ClassInfo'


class Department(models.Model):
    name = models.CharField(max_length = 100 , unique = True)
    department_select= (
        ('Science Department','Science Department'),
        ('Math Department','Math Department'),
        ('English Department','English Department'),
        ('Kiswahili Department','Kiswahili Department'),
        ('CRE Department','CRE Department'),
        ('Social-Studies Department','Social-Studies Department')
     
    )
    department = models.CharField(max_length = 30 ,choices = department_select)
    def __str__(self):
        """Returns the name of a department

        Returns:
            [type] -- [description]
        """
        return self.name

class ClassRegistration(models.Model):
    name = models.CharField(max_length = 10,unique=True)
    classinfo = models.ForeignKey(ClassInfo,on_delete=models.CASCADE ,max_length = 50 ,null = True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    class Meta():
        verbose_name_plural = 'ClassRegistration'
