# Generated by Django 4.0.5 on 2022-07-06 07:48

from django.db import migrations, models
from django.template.defaultfilters import slugify

DEFAULT=1000

def forwards(apps, _):
    Persona = apps.get_model("personas", "Persona")
    personas = Persona.objects.all()
    for persona in personas:
        persona.slug = slugify(persona.edad)
        persona.save()


def backwards(apps, _):
    Persona = apps.get_model("personas", "Persona")
    personas = Persona.objects.all()
    for persona in personas:
        persona.slug = DEFAULT
        persona.save()

class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_persona_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(default=DEFAULT),
            preserve_default=False,
        ),
        migrations.RunPython(forwards, backwards)
    ]
