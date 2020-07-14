"""Defines the url patterns for the parents app
    """

from django.urls import path
from . import views


#url conf
app_name = 'parent'

urlpatterns = [
    
    path('parent-registration/',views.parent_registration ,name='parent-registration'),
    path('profile/<str:parent_name>',views.parent_profile ,name='parent-profile'),
    path('parent-list/',views.parent_list ,name='parent-list'),
    path('edit/<str:parent_name>',views.parent_edit , name ='parent-edit'),
    path('delete/<str:parent_name>',views.parent_delete , name ='parent-delete'),

]
