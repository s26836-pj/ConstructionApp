from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import UserCreateView, UserPasswordResetView, UserUpdateView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

    path('<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),

]
