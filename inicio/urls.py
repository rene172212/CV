

from django.urls import path
from . import views

urlpatterns = [
    path("hola-mundo",views.index),
    path("acerca-de",views.about),
    path("contacto",views.contact),
]