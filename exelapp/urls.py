from django.contrib import admin
from django.urls import path,include

from.views import home,add_student
from . import views

urlpatterns = [
    path('', home),
        path('add_student', add_student),
        path('add_students', views.add_students, name='add_students'),
           path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'), 
     path('makeintime', views.makeintime, name='makeintime'), 
     path('makeouttime', views.makeouttime, name='makeouttime'),
     path('export_students_excel/', views.export_students_excel, name='export_students_excel'),

   
]
