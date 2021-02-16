from .models import Pista, Reserva, Horario, Tarifa
from rest_framework import serializers

class PistaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pista
        fields = ['url', 'deporte']

class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = ['url', 'reserva_usuario', 'reserva_horario']

class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ['url', 'fecha','hora', 'horario_pista', 'horario_tarifa']

class TarifaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarifa
        fields = ['url', 'definicion', 'precio']
