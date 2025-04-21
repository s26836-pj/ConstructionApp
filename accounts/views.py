from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import FormView
from pyexpat.errors import messages

from accounts.base_views import BaseAdminUpdateView, BaseAdminCreateView, BaseAdminListView, BaseLoginRequiredListView
from accounts.forms import CustomUserCreationForm, CustomUserUpdateForm, AdminUserUpdateForm
from accounts.models import CustomUser
from accounts.utils import send_activation_email


class UserCreateView(BaseAdminCreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/account_create.html'
    success_url = reverse_lazy('account_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_activation_email(self.object)
        return response

class UserListView(BaseLoginRequiredListView):
    model = get_user_model()
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'
    success_url = reverse_lazy('account_list')

class UserUpdateView(BaseAdminUpdateView):
    model = CustomUser
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('account_list')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return AdminUserUpdateForm
        return CustomUserUpdateForm

    def form_valid(self, form):
        # dodatkowe zabezpieczenie na backendzie (na wszelki wypadek)
        if not self.request.user.is_superuser:
            form.instance.role = self.get_object().role
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and self.get_object() != request.user:
            return redirect('account_list')  # lub 403
        return super().dispatch(request, *args, **kwargs)


class UserPasswordResetView(LoginRequiredMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class ActivateAccountView(FormView):
    template_name = 'accounts/activate_account.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('account_list')

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
        if form.cleaned_data.get('new_password1'):
            form.save()
            self.user.is_active = True
            self.user.save()
            messages.success(self.request, "Your account has been activated. You can now log in.")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Password was not set. Activation failed.")
            return redirect('login')
