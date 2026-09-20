

from django.urls import path
from . import views

urlpatterns = [
    path("<int:menu>",views.menu_hoja_number,name="menu_hoja_number"),
    path("<str:menu>",views.menu_hoja) #menu contacto
]