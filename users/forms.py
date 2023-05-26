from django import forms
from django.contrib.auth.forms import (
    UserChangeForm as DefaultUserChangeForm,
    UserCreationForm as DefaultUserCreationForm,
)

from .models import User


class UserCreationForm(DefaultUserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserChangeForm(DefaultUserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")
