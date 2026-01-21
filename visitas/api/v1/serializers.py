from django.utils.text import slugify
from rest_framework import serializers

from visitas.models import Visita


class VisitaSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        read_only=True,
        help_text='Gerado automaticamente a partir do nome do visitante e data da visita',
    )

    class Meta:
        model = Visita
        fields = [
            'codigo',
            'visitante_nome',
            'visitante_email',
            'data_visita',
            'slug',
        ]

    @staticmethod
    def validate(data) -> dict[str, str]:
        visitante_nome = data.get('visitante_nome', '')
        data_visita = data.get('data_visita', '')

        data['slug'] = slugify(f'{visitante_nome}-{data_visita}')
        return data
