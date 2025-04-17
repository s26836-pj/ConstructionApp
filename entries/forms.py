from django import forms

from entries.models import Entry


#to check later on
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['construction', 'operational_activity', 'content']
        widgets = {
            'construction': forms.Select(attrs={'class': 'form-control'}),
            'operational_activity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Czynność operacyjna'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Treść wpisu'}),
        }
