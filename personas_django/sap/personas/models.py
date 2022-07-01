from django.db import models

# Create your models here.
#Primero se crea la clase direccion ya que no depende de Persona para existir en este caso

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio= models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
    #El segundo parametro nos dice que va a suceder si se elimina un domicilio
    #que este asociado a la persona



    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'