from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def v1(request):
    return HttpResponse("<h1>App2 - Vista 1</h1><p>Contenido</p><a href='/app2/v2/'>Ir a v2</a>")

def v2(request):
    return HttpResponse("<h1>App2 - Vista 2</h1><p>Más contenido</p><a href='/app2/v1/'>Volver a v1</a>")
