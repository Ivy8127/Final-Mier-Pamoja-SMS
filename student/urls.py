"""Defines the url patterns for the students app
    """

from django.urls import path
from . import views


#url conf
app_name = 'student'

urlpatterns = [
    
    path('student-registration/',views.student_registration ,name='student-registration'),
    path('profile/<reg_no>',views.student_profile ,name='student-profile'),
    path('student-list/',views.student_list ,name='student-list'),
    path('edit/<reg_no>',views.student_edit , name ='student-edit'),
    path('delete/<int:reg_no>',views.student_delete , name ='student-delete'),
    path('student-search/', views.student_search, name='student-search'), 
    path('enrolled/', views.enrolled_student, name ='student-enrolled'),
    path('enrolled-student/<reg>',views.student_enrolled, name='enrolled' ),
    path('enrolled-student-list/',views.enrolled_student_list, name ='enrolled-student-list'),

]
