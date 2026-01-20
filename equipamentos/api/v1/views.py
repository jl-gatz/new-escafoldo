import uuid

from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from equipamentos.api.v1 import serializers
from equipamentos.models import Equipamento

# class EquipamentoListView(ListAPIView):
#     queryset = Equipamento.objects.all()
#     model = Equipamento
#     serializer_class = serializers.EquipamentoSerializer
#     context_object_name = 'equipamentos'
#     paginate_by = 10  # Número de equipamentos por página
#     ordering = ['marca', 'modelo']  # Ordenar por marca e modelo


# class EquipamentoSlugView(RetrieveUpdateDestroyAPIView):
#     queryset = Equipamento.objects.all()
#     model = Equipamento
#     serializer_class = serializers.EquipamentoSerializer
#     slug_url_kwarg = 'slug'

#     def get_object(self):
#         slug = self.kwargs.get(self.slug_url_kwarg)
#         return Equipamento.objects.get(slug=slug)


# class EquipamentoDetailViewById(RetrieveUpdateDestroyAPIView):
#     queryset = Equipamento.objects.all()
#     model = Equipamento
#     serializer_class = serializers.EquipamentoSerializer
#     context_object_name = 'equipamento'


class EquipamentosViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = serializers.EquipamentoSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        lookup_value = self.kwargs.get(self.lookup_field)

        filter_kwargs = {'slug': lookup_value}

        if self.is_valid_uuid(lookup_value):
            filter_kwargs = {'pk': lookup_value}

        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)

        return obj

    def is_valid_uuid(self, value):  # noqa: PLR6301
        try:
            uuid_obj = uuid.UUID(str(value), version=4)  # noqa: F841
            return True
        except ValueError:
            return False
