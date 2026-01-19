from django.urls import path

from .views import VisitaListView

urlpatterns = [
    path('', VisitaListView.as_view(), name='visita_list'),
]
