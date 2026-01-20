import uuid

from django.db import models


# Modelos do app visitas
class Visita(models.Model):
    codigo = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='id_visita',
    )
    visitante_nome = models.CharField(
        verbose_name='Nome do visitante', max_length=100, null=False
    )
    visitante_email = models.EmailField(
        verbose_name='Email do visitante', max_length=100, null=False
    )
    data_visita = models.DateTimeField(
        verbose_name='Data da visita', auto_now_add=False, null=False
    )
    slug = models.SlugField(null=False, unique=True, max_length=100)

    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        ordering = ['-data_visita']
        db_table = 'visitas'


class VisitaImagem(models.Model):
    visita = models.ForeignKey(
        Visita,
        on_delete=models.CASCADE,
        related_name='imagens',
        verbose_name='Visita relacionada',
    )
    imagem = models.ImageField(
        upload_to='static/media/visitas/', verbose_name='Imagem da visita'
    )

    class Meta:
        verbose_name = 'Imagem da Visita'
        verbose_name_plural = 'Imagens das Visitas'
        ordering = ['visita']
        db_table = 'visita_imagens'

    def __str__(self):
        return f'Imagem da visita {self.imagem.url}'
