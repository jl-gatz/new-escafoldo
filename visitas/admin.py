from django.contrib import admin

from .models import Visita


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = (
        'visitante_nome',
        'visitante_email',
        'data_visita',
    )
    search_fields = (
        'visitante_nome',
        'visitante_email',
    )
    ordering = ('-data_visita',)
