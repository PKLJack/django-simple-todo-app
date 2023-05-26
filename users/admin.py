from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

# Register your models here.


class UserAdmin(DefaultUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("id", "username", "email")


# admin.site.register(User)
admin.site.register(User, UserAdmin)
