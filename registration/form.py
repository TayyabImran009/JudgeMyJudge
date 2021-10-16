from django import forms
from person.models import contactMesages


class contactMesagesForm(forms.ModelForm):
    class Meta:
        model = contactMesages
        fields = ['name', 'email', 'subject', 'message']
