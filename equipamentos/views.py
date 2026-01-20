from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from equipamentos import serializers

from .models import Equipamento


class EquipamentoListView(ListAPIView):
    queryset = Equipamento.objects.all()
    model = Equipamento
    serializer_class = serializers.EquipamentoSerializer
    context_object_name = 'equipamentos'
    paginate_by = 10  # Número de equipamentos por página
    ordering = ['marca', 'modelo']  # Ordenar por marca e modelo


class EquipamentoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Equipamento.objects.all()
    model = Equipamento
    serializer_class = serializers.EquipamentoSerializer
    context_object_name = 'equipamento'
