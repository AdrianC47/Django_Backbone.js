from django.forms import modelform_factory
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
import json
# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)  # esto se lo hace en caso que no encuentre un id
    return render(request, 'personas/detalle.html', {'persona': persona})


# PersonaForm = modelform_factory(Persona, exclude=[])  ##clase generada a partir de Persona, no se excluye ningun atributo


def nuevaPersona(request):
    # si el objeto request en su atributo de metodo se envio la info de tipo POST quiere decir que se debe procesar
    # el formulario de lo contrario quiere decir que es 1ra vez que se hace la peticion a esta pagina y por lo tanto
    # debemos crear un nuevo objeto de tipoformulario y hacer el render a la pagina
    if request.method == 'POST':
        # se procesa la info del formulario creando un nuevo obj Persona con la info del formulario(request)
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else:
        formaPersona = PersonaForm()  # se crea una nueva instancia de la clase creada arriba PersonaForm

        return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST,
                                   instance=persona)  ##para el actualizar tambien se manda como parametro la instancia
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else:

        formaPersona = PersonaForm(instance=persona)

        return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


def eliminarPersona(request, id):
    # se obtiene el id y por medio del mismo busco al objeto
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('inicio')


def listarPersona(request, id):
    if(id>0):
        c = list(Persona.objects.filter(id=id).values())
        if len(c) > 0:
            com = c[0]
            datos = {'mensaje': "Exitoso", 'Persona': com}
        else:
            datos = {'message': "Persona no encontrada.."}
        return JsonResponse(datos)
    else:
        c = list(Persona.objects.values())  
        if len(c)>0:    
            datos = {'mensaje': "Exitoso", 'Persona': c}
        else:
           datos = {'message': "Persona no encontrada.."}
        return JsonResponse(datos)     
    #objetoJson=JsonResponse(datos)
    #return render(request, 'personas/detalle.html', {'persona': objetoJson})
    