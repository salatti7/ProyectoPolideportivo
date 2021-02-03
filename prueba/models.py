from django.db import models

# Create your models here.
class Deporte(models.Model):
    nombre=models.CharField(max_length=35)
    descripccion=models.CharField(max_length=35)
    num_jugadores=models.IntegerField() 


class TipoPelota(models.Model):
    tipo=models.CharField(max_length=25)
    tipo_pelota_deporte=models.ForeignKey(Deporte, on_delete=models.CASCADE)