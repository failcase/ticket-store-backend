from django import forms
from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm
from .models import CustomUser

class CustomAdminUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"