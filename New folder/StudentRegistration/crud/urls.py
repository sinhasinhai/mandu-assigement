from django.urls import path, include
from django.conf import settings
from crud import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studentList', views.studentList, name='studentList'),
    path('delete/<int:id>/', views.deleteData, name='deleteData'),
    path('update/<int:id>/', views.updateStudent, name='updateStudent'),
]