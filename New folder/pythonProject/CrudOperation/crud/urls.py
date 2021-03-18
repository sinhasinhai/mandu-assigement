from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.studentList, name='index'),
    path('studentForm', views.studentForm, name='studentForm'),
    path('edit/<int:id>/', views.editStudent, name='editStudent'),
    path('delete/<int:id>/', views.deleteData, name='deleteData'),
    path('update<int.id>/', views.updateStudent, name='updateStudent'),
]