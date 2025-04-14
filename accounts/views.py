from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import CustomUserCreationForm, CustomUserUpdateForm


class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/user_create.html'
    success_url = reverse_lazy('user_list') # tutaj scizka do zmiany

    def form_valid(self, form):
        # Tutaj możesz dodać logikę wysyłania maila z aktywacją po zapisaniu konta
        response = super().form_valid(form)
        # np. wywołaj funkcję wysyłającą email aktywacyjny
        # send_activation_email(self.object)
        return response

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    form_class = CustomUserUpdateForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('user_list')

class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')


