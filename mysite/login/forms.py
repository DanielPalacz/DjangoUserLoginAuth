from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", help_text="Required. It has to be email-like format.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
