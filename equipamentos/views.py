from django.views.generic import DetailView, ListView

from .models import Equipamento


class EquipamentoListView(ListView):
    queryset = Equipamento.objects.all()
    model = Equipamento
    template_name = 'equipamentos/equipamento_list.html'
    context_object_name = 'equipamentos'
    paginate_by = 10  # Número de equipamentos por página
    ordering = ['marca', 'modelo']  # Ordenar por marca e modelo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EquipamentoDetailView(DetailView):
    model = Equipamento
    template_name = 'equipamentos/equipamento_detail.html'
    context_object_name = 'equipamento'
    pk_url_kwarg = 'equipamento_id'  # 'equipamento_id' eh PK

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # detail = Equipamento.objects.filter(slug=self.kwargs.get('slug'))

        return context
