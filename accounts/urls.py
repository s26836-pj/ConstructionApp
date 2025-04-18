from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import UserCreateView, UserPasswordResetView, UserUpdateView, ActivateAccountView, UserListView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='account_create'),
    path('list/', UserListView.as_view(), name='account_list'),
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

    path('<int:pk>/edit/', UserUpdateView.as_view(), name='account_update'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate_account'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
