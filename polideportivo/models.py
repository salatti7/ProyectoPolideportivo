from django.db import models
from django.contrib.auth.models import User

tipo_tarifa = (
    ('mañana', 'mañana'),
    ('tarde','tarde')
)

class Pista(models.Model):
    deporte = models.CharField(max_length = 50)
    imagen = models.ImageField(upload_to="polideportivo/images")
    descripcion = models.TextField()
    precio = models.IntegerField()

    def __str__(self):
        return self.deporte

    class Meta:
        verbose_name = 'Pista'
        verbose_name_plural = 'Pistas'


class Tarifa(models.Model):
    definicion = models.CharField(choices = tipo_tarifa, max_length = 50)
    precio = models.IntegerField()

    def __str__(self):
        return self.definicion

    class Meta:
        verbose_name = 'Tarifa'
        verbose_name_plural = 'Tarifas'

class Horario(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()

    horario_pista = models.ForeignKey('Pista', on_delete = models.CASCADE)
    horario_tarifa = models.ForeignKey('Tarifa', on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.fecha) + " " + str(self.hora)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

class Reserva(models.Model):
    reserva_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    email_cliente = models.CharField(max_length=100)
    dni_cliente = models.CharField(max_length=50)
    precio_final = models.IntegerField()

    def str(self):
        return str(self.nombre_cliente) + " " + str(self.apellido_cliente) + " " + str(self.fecha) + " " + str(self.hora)


    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
