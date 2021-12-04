from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=TextInput(attrs={'placeholder': 'пароль',
                                           'class': "input-field"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=TextInput(attrs={'placeholder': 'повт. пароль',
                                           'class': "input-field"}),
        strip=False,
        help_text=("подтвердите пароль"),
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        error_messages = {
            'password_mismatch': ('The two password fields didn’t match.'),
        }
        widgets = {
            'username': TextInput(attrs={'placeholder': 'имя пользователя',
                                           'class': "input-field"}),
            'email': TextInput(attrs={'placeholder': 'почта',
                                           'class': "input-field"}),
            'first_name': TextInput(attrs={'placeholder': 'имя',
                                           'class': "input-field"}),
            'last_name': TextInput(attrs={'placeholder': 'фамилия',
                                           'class': "input-field"}),
            'password1': TextInput(attrs={'placeholder': 'пароль',
                                           'class': "input-field"}),
            'password2': TextInput(attrs={'placeholder': 'повт. пароль',
                                           'class': "input-field"}),
        }
