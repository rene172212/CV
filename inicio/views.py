from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hola, bienvenido a mi hoja de vida desde Django!")

def about(request):
    return HttpResponse("Esta es la sección acerca de mi hoja de vida desde Django!")

def contact(request):
    return HttpResponse("Esta es la sección de contacto de mi hoja de vida desde Django!")