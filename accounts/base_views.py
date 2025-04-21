from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib import messages


class BaseLoginRequiredView(LoginRequiredMixin, View):
    pass


class BaseAdminOnlyView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)


class BaseAdminCreateView(BaseAdminOnlyView, CreateView):
    pass

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)

class BaseAdminUpdateView(BaseAdminOnlyView, UpdateView):
    pass

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)

class BaseAdminListView(BaseAdminOnlyView, ListView):
    pass

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)

class BaseLoginRequiredListView(LoginRequiredMixin, ListView):
    pass