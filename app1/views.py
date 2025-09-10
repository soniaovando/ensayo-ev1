from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def v1(request):
    return HttpResponse("<h1>App1 - Vista 1</h1><p>Texto</p><a href='/app1/v2/'>Ir a v2</a>")

def v2(request):
    return HttpResponse("<h1>App1 - Vista 2</h1><p>Otro texto</p><a href='/app1/v1/'>Volver a v1</a>")
