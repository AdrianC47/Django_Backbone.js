from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404

# Create your views here.
from personas.models import Persona


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)  # esto se lo hace en caso que no encuentre un id
    return render(request, 'personas/detalle.html', {'persona': persona})


PersonaForm = modelform_factory(Persona, exclude=[])  ##clase generada a partir de Persona, no se excluye ningun atributo


def nuevaPersona(request):
    formaPersona = PersonaForm()  # se crea una nueva instancia de la clase creada arriba PersonaForm
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})
