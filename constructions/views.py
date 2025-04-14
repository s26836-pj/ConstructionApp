from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from .forms import (
    ConstructionCreateForm,
    ConstructionUpdateForm,
    ConstructionArchiveForm
)
from .models import Construction


# Widok listy budów – domyślnie pokazuje tylko aktywne budowy (is_archived=False);
# administrator może przełączyć się na wyświetlanie zarchiwizowanych za pomocą parametru GET.
class ConstructionListView(ListView):
    model = Construction
    template_name = 'constructions/construction_list.html'
    context_object_name = 'constructions'

    def get_queryset(self):
        qs = super().get_queryset()
        show_archived = self.request.GET.get('show_archived', 'false').lower()

        if show_archived == 'true':
            # Pokaż TYLKO zarchiwizowane
            return qs.filter(is_archived=True)
        else:
            # Pokaż TYLKO aktywne
            return qs.filter(is_archived=False)


# Widok tworzenia budowy
class ConstructionCreateView(CreateView):
    form_class = ConstructionCreateForm
    template_name = 'constructions/construction_form.html'
    success_url = reverse_lazy('construction_list')


# Widok edycji budowy (bez archiwizacji)
class ConstructionUpdateView(UpdateView):
    model = Construction
    form_class = ConstructionUpdateForm
    template_name = 'constructions/construction_form.html'
    success_url = reverse_lazy('construction_list')


# Widok archiwizacji budowy – zamiast usuwania budowy, administrator może ją zarchiwizować.
# Używamy dedykowanego formularza, który umożliwia podanie (opcjonalnie) powodu archiwizacji.
class ConstructionArchiveView(UpdateView):
    model = Construction
    form_class = ConstructionArchiveForm
    template_name = 'constructions/construction_archive.html'
    success_url = reverse_lazy('construction_list')

    def form_valid(self, form):
        form.instance.is_archived = True
        return super().form_valid(form)
