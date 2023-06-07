from django.db import models

# Create your models here.

class Person(models. Models):
    nombre = models. CharField(max_length=50)
    apellido = models. CharField(max_length=50)
    correoelectrónico = models. CharField(max_length=50)
    activo = models. BooleanField(default=True)

    def __str__(self):
        return f'id:{self. id} - {self. nombre} {self. apellido}'