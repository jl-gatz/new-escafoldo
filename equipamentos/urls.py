from django.urls import path

from .views import (
    EquipamentoDetailViewById,
    EquipamentoListView,
    EquipamentoSlugView,
)

urlpatterns = [
    path('', EquipamentoListView.as_view(), name='equipamento_list'),
    path(
        '<uuid:pk>/',
        EquipamentoDetailViewById.as_view(),
        name='equipamento_detail_by_id',
    ),
    path(
        '<slug:slug>/',
        EquipamentoSlugView.as_view(),
        name='equipamento_slug',
    ),
]
