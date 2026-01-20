from django.contrib import admin

from .models import Visita, VisitaImagem


class VisitaImagemInline(admin.StackedInline):
    model = VisitaImagem
    extra = 1


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
    prepopulated_fields = {'slug': ('visitante_nome', 'data_visita')}
    inlines = [VisitaImagemInline]
