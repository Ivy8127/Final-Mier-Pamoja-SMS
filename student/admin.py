from django.contrib import admin
from student.models import *

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(AcademicInfo)
admin.site.register(EnrolledStudent)