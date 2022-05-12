#from xml.etree.ElementInclude import include
#from django.contrib import admin
from django.urls import path
from AppIdiomaOnline import views


urlpatterns = [
    path('',views.index, name="Index"),
    path('cursos', views.courses, name="Cursos"),
    path('profesores', views.teachers, name="Profesores"),
    path('estudiantes', views.students, name="Estudiantes"),
    path('practicas', views.practice, name="Practicas"),
]



