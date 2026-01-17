from django.urls import path

from .views import EquipamentoDetailView, EquipamentoListView

urlpatterns = [
    path('', EquipamentoListView.as_view(), name='equipamento_list'),
    path(
        '<slug:slug>/',
        EquipamentoDetailView.as_view(),
        name='equipamento_detail',
    ),
    path(
        '<int:equipamento_id>/',
        EquipamentoDetailView.as_view(),
        name='equipamento_detail_by_id',
    ),
]
