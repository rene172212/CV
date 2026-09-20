from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("Hola, bienvenido a mi hoja de vida desde Django!")

def menu_hoja_number(request, menu):
    inicio_text = None
    if menu == 1:
        inicio_text = "Bienvenido a mi hoja de vida"
    elif menu == 2:
        inicio_text = "Acerca de mi hoja de vida"
    elif menu == 3:
        inicio_text = "Contacto de mi hoja de vida"
    else:
        inicio_text = "Opción no válida"
        return HttpResponseNotFound(inicio_text)
    return HttpResponse(inicio_text)

def menu_hoja(request, menu):
    inicio_text = None
    if menu == "inicio":
        inicio_text = "Bienvenido a mi hoja de vida"
    elif menu == "acerca-de":
        inicio_text = "Acerca de mi hoja de vida"
    elif menu == "contacto":
        inicio_text = "Contacto de mi hoja de vida"
    else:
        inicio_text = "Opción no válida"
        return HttpResponseNotFound(inicio_text)
    return HttpResponse(inicio_text)