from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

        def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)

            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = "form-control"


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'address',
                  'case_number', 'picture_id']

        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'form-control'}),
        }
 