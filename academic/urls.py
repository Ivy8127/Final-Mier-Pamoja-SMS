from django.urls import path
from . import views

app_name = 'academic'

urlpatterns = [
    path('class-registration/', views.class_registration, name="class-registration"),
    path('create-class/', views.add_class, name="create-class"),
    path('class-list/', views.class_list, name='class-list'),
    

    

]