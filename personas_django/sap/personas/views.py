from django.shortcuts import render, get_object_or_404

# Create your views here.
from personas.models import Persona


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id) #esto se lo hace en caso que no encuentre un id
    return render(request, 'personas/detalle.html', {'persona': persona})
