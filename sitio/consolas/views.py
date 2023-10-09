from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
"""
def index(request):
    return HttpResponse("Hola Mundo!")
"""
def index(request):
    params = {}
    params['nombre_sitio'] = 'consolas'
    return render(request, 'index.html', params)