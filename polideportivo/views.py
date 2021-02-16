from .models import Pista, Reserva, Horario, Tarifa
from rest_framework import viewsets
from .serializers import PistaSerializer, HorarioSerializer, ReservaSerializer, TarifaSerializer


class PistaViewSet(viewsets.ModelViewSet):

    queryset = Pista.objects.all()
    serializer_class = PistaSerializer

class HorarioViewSet(viewsets.ModelViewSet):

    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class ReservaViewSet(viewsets.ModelViewSet):

    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class TarifaViewSet(viewsets.ModelViewSet):

    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer