from django.urls import reverse_lazy
from django.views.generic import DetailView

from accounts.base_views import BaseLoginRequiredView
from accounts.views import (
    BaseAdminCreateView,
    BaseAdminUpdateView,
    BaseLoginRequiredListView
)
from .forms import (
    ConstructionCreateForm,
    ConstructionUpdateForm,
    ConstructionArchiveForm
)
from .models import Construction


class ConstructionListView(BaseLoginRequiredListView):
    model = Construction
    template_name = 'constructions/construction_list.html'
    context_object_name = 'constructions'
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        show_archived = self.request.GET.get('show_archived', 'false').lower()

        if show_archived == 'true':
            return qs.filter(is_archived=True)
        else:
            return qs.filter(is_archived=False)


# Widok tworzenia budowy
class ConstructionCreateView(BaseAdminCreateView):
    form_class = ConstructionCreateForm
    template_name = 'constructions/construction_form.html'
    success_url = reverse_lazy('construction_list')


# Widok edycji budowy (bez archiwizacji)
class ConstructionUpdateView(BaseAdminUpdateView):
    model = Construction
    form_class = ConstructionUpdateForm
    template_name = 'constructions/construction_form.html'
    success_url = reverse_lazy('construction_list')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_archived=False)

class ConstructionArchiveView(BaseAdminUpdateView):
    model = Construction
    form_class = ConstructionArchiveForm
    template_name = 'constructions/construction_archive.html'
    success_url = reverse_lazy('construction_list')

    def form_valid(self, form):
        form.instance.is_archived = True
        return super().form_valid(form)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_archived=False)

class ConstructionDetailView(BaseLoginRequiredView, DetailView):
    model = Construction
    template_name = 'constructions/construction_detail.html'
    context_object_name = 'construction'
