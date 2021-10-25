from django import forms
from .models import bestInterest, judgeRateing


class bestInterestForm(forms.ModelForm):
    class Meta:
        model = bestInterest
        exclude = ('user', 'ratedTo')


class judgeRateingForm(forms.ModelForm):
    class Meta:
        model = judgeRateing
        exclude = ('user', 'ratedTo', 'total_likes',
                   'total_dislikes', 'likeBy', 'dislikeBy')
