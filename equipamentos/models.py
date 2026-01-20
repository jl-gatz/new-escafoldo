from django.db import models


# Modelos do app equipamentos
class Equipamento(models.Model):
    codigo = models.UUIDField(
        primary_key=True,
        default=models.UUIDField,
        editable=False,
        verbose_name='id_equipamentos',
    )
    descricao = models.CharField(
        verbose_name='Descrição do equipamento', max_length=144, null=True
    )
    imagem = models.ImageField(
        upload_to='static/media/equips/', default=None, null=True
    )
    marca = models.CharField(verbose_name='Marca', max_length=40, null=True)
    modelo = models.CharField(verbose_name='Modelo', max_length=40, null=True)
    slug = models.SlugField(null=True)
    url = models.URLField(
        verbose_name='Link para o equipamento',
        max_length=200,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
        ordering = ['codigo']
        db_table = 'equipamentos'
