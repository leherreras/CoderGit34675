from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def saludo(request):
    return HttpResponse("Hola Django - Coder")


def mostrar_html(request):
    return HttpResponse("<button>este mi boton</button><br><h1>Hola</h1>")


def retornar_parametro(request):
    mensaje = f"La fecha de hoy es {datetime.now()}"
    return HttpResponse(mensaje)


def mi_nombre(request, nombre):
    """
    View to show the name
    Args:
        request: request from the GUI
        nombre: the name of the people

    Returns:
        return httpResponse with the name
    """
    return HttpResponse(f"Hola, bienvenido <b>{nombre}</b>")


def show_html(request):
    return render(request, "template1.html")


def show_html2(request):
    return render(request, "template2.html")
