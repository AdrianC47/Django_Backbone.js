from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    #mensajes = {'msg1':'Valor mensaje 1', 'msg2':'Valor mensaje 2'}
    #return HttpResponse('Hola mundo desde Django')
    no_personas_var = Persona.objects.count();
    return render(request, 'bienvenido.html', {'no_personas':no_personas_var})


# def despedirse(request):
#     return  HttpResponse('Eso es todo amigos')
#
# def contacto(request):
#     return HttpResponse('Luis Adrián Cabrera - lcabrerab@est.ups.edu.ec')