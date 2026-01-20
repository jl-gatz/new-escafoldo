from rest_framework.generics import ListAPIView

from visitas import serializers

from .models import Visita


class VisitaListView(ListAPIView):
    queryset = Visita.objects.all()
    model = Visita
    context_object_name = 'visitas'
    serializer_class = serializers.VisitaSerializer
    paginate_by = 10  # Número de visitas por página
    ordering = ['-data_visita']  # Ordenar por data da visita, mais recente
