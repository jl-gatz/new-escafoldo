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


class EquipamentoSlugView(RetrieveUpdateDestroyAPIView):
    queryset = Equipamento.objects.all()
    model = Equipamento
    serializer_class = serializers.EquipamentoSerializer
    slug_url_kwarg = 'slug'

    def get_object(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        return Equipamento.objects.get(slug=slug)


class EquipamentoDetailViewById(RetrieveUpdateDestroyAPIView):
    queryset = Equipamento.objects.all()
    model = Equipamento
    serializer_class = serializers.EquipamentoSerializer
    context_object_name = 'equipamento'
