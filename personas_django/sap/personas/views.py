from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)  # esto se lo hace en caso que no encuentre un id
    return render(request, 'personas/detalle.html', {'persona': persona})


#PersonaForm = modelform_factory(Persona, exclude=[])  ##clase generada a partir de Persona, no se excluye ningun atributo


def nuevaPersona(request):
    #si el objeto request en su atributo de metodo se envio la info de tipo POST quiere decir que se debe procesar
    #el formulario de lo contrario quiere decir que es 1ra vez que se hace la peticion a esta pagina y por lo tanto
    #debemos crear un nuevo objeto de tipoformulario y hacer el render a la pagina
    if request.method == 'POST':
        #se procesa la info del formulario creando un nuevo obj Persona con la info del formulario(request)
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else:
        formaPersona = PersonaForm()  # se crea una nueva instancia de la clase creada arriba PersonaForm

        return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})
