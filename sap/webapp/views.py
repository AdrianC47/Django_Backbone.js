from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def despedirse(request):
    return  HttpResponse('Eso es todo amigos')

def contacto(request):
    return HttpResponse('Luis Adrián Cabrera - lcabrerab@est.ups.edu.ec')