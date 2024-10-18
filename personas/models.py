from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=[('F', 'Femenino'), ('M', 'Masculino')])
    edad = models.IntegerField()
    altura = models.IntegerField()
    peso = models.IntegerField()
    cintura = models.IntegerField()
    abdomen = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
