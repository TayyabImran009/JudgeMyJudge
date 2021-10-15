from django import forms
from .models import bestInterest


class bestInterestForm(forms.ModelForm):
    class Meta:
        model = bestInterest
        exclude = ('user', 'ratedTo')
