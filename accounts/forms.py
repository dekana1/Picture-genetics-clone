from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


class RegistrationUserForm(UserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={
            'class': 'login-input',
            'style': 'max-width: 350px',
        }
    ))
    password2 = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={
            'class': 'login-input',
            'style': 'max-width: 350px',
        }
    ))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'first_name': TextInput(attrs={
                'class': "login-input",
                'style': 'max-width: 300px;',

            }),
            'last_name': TextInput(attrs={
                'class': "login-input",
                'style': 'max-width: 300px;',

            }),
            'email': EmailInput(attrs={
                'class': "login-input",
                'style': 'max-width: 350px;',

            }),
            'password1': PasswordInput(attrs={
                'class': "login-input",
                'style': 'max-width: 350px;',

            }),
            'password2': PasswordInput(attrs={
                'class': "login-input",
                'style': 'max-width: 350px;',

            }),
        }


class UserLoginForm(ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={
            'class': 'login-input',
            'style': 'max-width: 300px',
        }
    ))

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': EmailInput(attrs={
                'class': "login-input",
                'style': 'max-width: 300px;',

            }),
            'password': PasswordInput(attrs={
                'class': "login-input",

            })
        }

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Credentials!')
