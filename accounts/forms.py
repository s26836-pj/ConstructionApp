from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'position']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'position']


class AdminUserUpdateForm(forms.ModelForm):
    """Formularz dla administratora – z polem 'role'."""
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'position', 'role']
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'})
            for field in ['first_name', 'last_name', 'email', 'position']
        }
        widgets.update({
            'role': forms.Select(attrs={'class': 'form-control'})
        })

class CustomUserUpdateForm(forms.ModelForm):
    """Formularz dla zwykłych użytkowników – bez pola 'role'."""
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'position']
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'}) for field in fields
        }