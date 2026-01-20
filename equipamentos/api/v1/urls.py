from django.urls import path

from equipamentos.api.v1.views import EquipamentosViewSet

urlpatterns = [
    path('<str:pk>/', EquipamentosViewSet.as_view({'get': 'retrieve'})),
]
