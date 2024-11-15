from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # first_name, last_name, phone (no phone in class User fields)
    # last_login, date_joined ?

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]