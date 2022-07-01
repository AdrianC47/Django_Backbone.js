from django.contrib import admin

# Register your models here.
#Aqui registro mis modelos
from personas.models import Persona, Domicilio
admin.site.register(Persona)
admin.site.register(Domicilio)
