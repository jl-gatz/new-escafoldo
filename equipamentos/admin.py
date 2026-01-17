# Register your models here.
from django.contrib import admin

from .models import Equipamento


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'slug',)
    prepopulated_fields = {'slug': ('marca', 'modelo')}
    search_fields = ('marca', 'modelo')
    ordering = ('marca', 'modelo',)
