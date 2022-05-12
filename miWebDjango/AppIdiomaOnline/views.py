from django.http import HttpResponse
from django.shortcuts import render
from AppIdiomaOnline.forms import CursoForm


# Create your views here.

def index(request):
    return render(request, "AppIdiomaOnline/index.html")

#------------------------Clases
def courses(request):
    return render(request, "AppIdiomaOnline/cursos.html")

def teachers(request):
    return render(request, "AppIdiomaOnline/profesores.html")

def students(request):
    return render(request, "AppIdiomaOnline/estudiantes.html")

def practice(request):
    return render(request, "AppIdiomaOnline/practicas.html")

#---------------------------Formularios


