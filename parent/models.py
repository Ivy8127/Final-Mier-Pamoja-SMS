from django.db import models


# Create your models here.
class Personalinfo(models.Model):
    """Provides personal information about each and every parent

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    name = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to = 'parent-photos/',blank = True,null =True)
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
        ('other','Other')
    )
    religion = models.CharField(choices = religion_choice,max_length = 50)
    RELATIONSHIP =[
        ('Mother','Mother'),
        ('Father','Father'),
        ('Guardian','Guardian')
    ]
    relationship_to_student = models.CharField(max_length = 50 ,choices=RELATIONSHIP, default='Mother')
    parent_to = models.CharField(max_length =100)
    is_delete = models.BooleanField(default=False)
    

    def __str__(self):
        
        """Return a string representation of a parent's name

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


