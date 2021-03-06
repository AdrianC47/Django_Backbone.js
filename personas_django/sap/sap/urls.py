"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personas.views import detallePersona, nuevaPersona, editarPersona, eliminarPersona,listarPersona
from webapp.views import bienvenido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='inicio'),
    path('Listas/<int:id>', listarPersona),
    path('Nueva_Persona', nuevaPersona),
    path('Editar_Persona/<int:id>', editarPersona),
    path('Eliminar_Persona/<int:id>', eliminarPersona),
    #path('Listar_Persona/<int:id>', detallePersona),
    path('detalle_persona/<int:id>', detallePersona),

    # path('bienvenido/',bienvenido)
    # path('despedida.html', despedirse),
    # path('contacto', contacto)
]
