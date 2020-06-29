from django.db import models

# Create your models here.
class Designation(models.Model):
    """Role of users in the system

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    name = models.CharField(max_length = 100,unique = True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name