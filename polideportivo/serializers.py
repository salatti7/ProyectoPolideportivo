from .models import Pista, Reserva, Horario, Tarifa
from rest_framework import serializers

class PistaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pista
        fields = ['url', 'deporte', 'imagen', 'descripcion','precio']

class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = ['url', 'reserva_usuario', 'fecha', 'hora', 'nombre_cliente', 'apellido_cliente', 'email_cliente', 'dni_cliente', 'precio_final']

class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ['url', 'fecha','hora', 'horario_pista', 'horario_tarifa']

class TarifaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarifa
        fields = ['url', 'definicion', 'precio']

