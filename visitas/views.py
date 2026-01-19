from django.views.generic import ListView

from visitas import serializers

from .models import Visita


class VisitaListView(ListView):
    queryset = Visita.objects.all()
    model = Visita
    template_name = 'visitas/visita_list.html'
    context_object_name = 'visitas'
    serializer_class = serializers.VisitaSerializer
    paginate_by = 10  # Número de visitas por página
    ordering = ['-data_visita']  # Ordenar por data da visita, mais recente
