from django.forms import ModelForm, EmailInput

from personas.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = { ##aqui se indican los tipos de datos del formulario HTML
            'email': EmailInput(attrs:={'type': 'email'})
        }