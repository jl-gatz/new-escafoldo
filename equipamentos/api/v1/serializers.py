from rest_framework import serializers

from equipamentos.models import Equipamento


class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = '__all__'
