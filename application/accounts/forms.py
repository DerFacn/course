from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Логін", max_length=30, required=True, error_messages={'required': "Це поле обов'язкове!"})
    first_name = forms.CharField(label="Ім'я", max_length=30, required=True, error_messages={'required': "Це поле обов'язкове!"})
    last_name = forms.CharField(label="Прізвище", max_length=30, required=True, error_messages={'required': "Це поле обов'язкове!"})
    email = forms.EmailField(label="Електронна адреса", max_length=254,required=True, error_messages={'required': "Це поле обов'язкове!"})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
