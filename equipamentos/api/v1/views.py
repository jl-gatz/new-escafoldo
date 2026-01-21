import uuid

from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from equipamentos.api.v1 import serializers
from equipamentos.models import Equipamento


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

    @staticmethod
    def is_valid_uuid(value):
        try:
            uuid_obj = uuid.UUID(str(value), version=4)  # noqa: F841
            return True
        except ValueError:
            return False
