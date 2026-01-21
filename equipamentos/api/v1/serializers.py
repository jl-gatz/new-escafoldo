from django.utils.text import slugify
from rest_framework import serializers

from equipamentos.models import Equipamento


class EquipamentoSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        read_only=True,
        help_text='Gerado automaticamente a partir de marca e modelo',
    )

    class Meta:
        model = Equipamento
        fields = [
            'codigo',
            'descricao',
            'imagem',
            'marca',
            'modelo',
            'slug',
            'url',
        ]

        @staticmethod
        def validate(data) -> dict[str, str]:
            marca = data.get('marca', '')
            modelo = data.get('modelo', '')

            data['slug'] = slugify(f'{marca}-{modelo}')
            return data
