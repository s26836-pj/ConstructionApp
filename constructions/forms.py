from django import forms
from constructions.models import Construction

class ConstructionCreateForm(forms.ModelForm):
    class Meta:
        model = Construction
        fields = ['name', 'location', 'description', 'working_hours']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter construction name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'working_hours': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '08:00-17:00'}),
        }

class ConstructionUpdateForm(forms.ModelForm):
    class Meta:
        model = Construction
        fields = ['name', 'location', 'description', 'working_hours']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'working_hours': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Dedykowany formularz archiwizacji – administrator może wpisać powód archiwizacji (pole opcjonalne)
class ConstructionArchiveForm(forms.ModelForm):
    class Meta:
        model = Construction
        fields = ['archive_reason']
        widgets = {
            'archive_reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Powód archiwizacji (opcjonalnie)'}),
        }
