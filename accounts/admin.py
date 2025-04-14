from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('position', 'role')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
