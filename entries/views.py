from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic import UpdateView, DeleteView, DetailView

from entries.models import Entry


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'
    context_object_name = 'entry'


class EntryListView(ListView):
    model = Entry
    template_name = 'entries/entry_list.html'
    context_object_name = 'entries'
    paginate_by = 20  # Opcjonalnie: paginacja listy wpisów

    def get_queryset(self):
        qs = super().get_queryset().order_by('-created_at')

        # Pobieramy parametry wyszukiwania z GET
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        author = self.request.GET.get('author')  # np. username lub id
        construction = self.request.GET.get('construction')
        content = self.request.GET.get('content')
        operational_activity = self.request.GET.get('operational_activity')

        # Filtrowanie wpisów w zależności od podanych parametrów
        if start_date and end_date:
            qs = qs.filter(created_at__date__gte=start_date, created_at__date__lte=end_date)
        if author:
            qs = qs.filter(author__username__icontains=author)
        if construction:
            qs = qs.filter(construction__id=construction)
        if content:
            qs = qs.filter(content__icontains=content)
        if operational_activity:
            qs = qs.filter(operational_activity__icontains=operational_activity)

        return qs

class EntryCreateView(CreateView):
    model = Entry
    template_name = 'entries/entry_create.html'
    context_object_name = 'entry'
    success_url = reverse_lazy('entry_list')

class EntryUpdateView(UpdateView):
    model = Entry
    template_name = 'entries/entry_update.html'
    context_object_name = 'entry'
    success_url = reverse_lazy('entry_list')


class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'entries/entry_delete.html'
    context_object_name = 'entry'
    success_url = reverse_lazy('entry_list')
