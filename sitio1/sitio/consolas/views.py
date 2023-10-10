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

def preview(request):
    params = {}
    params['nombre_sitio'] = 'consolas'
    return render(request, 'preview.html', params)

def register(request):
    params = {}
    params['nombre_sitio'] = 'consolas'
    return render(request, 'register.html', params)

def login(request):
    params = {}
    params['nombre_sitio'] = 'consolas'
    return render(request, 'login.html', params)

def logout(request):
    params = {}
    params['nombre_sitio'] = 'consolas'
    return render(request, 'logout.html', params)
