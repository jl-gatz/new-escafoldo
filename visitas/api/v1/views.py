from rest_framework import viewsets

from visitas.api.v1 import serializers
from visitas.models import Visita


class VisitasViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = serializers.VisitaSerializer
    ordering = ['-data_visita']  # Ordenar por data da visita, mais recente
