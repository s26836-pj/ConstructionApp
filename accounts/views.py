from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from pyexpat.errors import messages

from accounts.forms import CustomUserCreationForm, CustomUserUpdateForm
from accounts.utils import send_activation_email
from django.contrib import messages


class UserCreateView(LoginRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/account_create.html'
    success_url = reverse_lazy('account_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_activation_email(self.object)
        return response

class UserListView(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'
    success_url = reverse_lazy('account_list')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserUpdateForm
    template_name = 'accounts/account_update.html'
    success_url = reverse_lazy('account_list')

class UserPasswordResetView(LoginRequiredMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class ActivateAccountView(LoginRequiredMixin, FormView):
    template_name = 'accounts/activate_account.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('user_list')  # możesz zmienić na 'user_list' jeśli wolisz

    def dispatch(self, request, *args, **kwargs):
        self.uidb64 = kwargs.get('uidb64')
        self.token = kwargs.get('token')
        try:
            uid = force_str(urlsafe_base64_decode(self.uidb64))
            self.user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            self.user = None

        if self.user is not None and default_token_generator.check_token(self.user, self.token):
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, "The activation link is invalid or has expired.")
            return redirect('login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your password has been set. You can now log in.")
        return super().form_valid(form)
