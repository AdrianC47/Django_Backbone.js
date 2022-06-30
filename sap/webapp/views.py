from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    mensajes = {'msg1':'Valor mensaje 1', 'msg2':'Valor mensaje 2'}
    #return HttpResponse('Hola mundo desde Django')
    return render(request, 'bienvenido.html', mensajes)
def despedirse(request):
    return  HttpResponse('Eso es todo amigos')

def despedirse(request):
    return  HttpResponse('Eso es todo amigos')

def contacto(request):
    return HttpResponse('Luis Adrián Cabrera - lcabrerab@est.ups.edu.ec')