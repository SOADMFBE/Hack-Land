from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, Group


from .models import *


class CreateUserForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),required=True, to_field_name="name")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2', 'group']

class ExpertForm(ModelForm):
    class Meta:
        model = teams
        fields = ['cp1', 'com1', 'cp2', 'com2']
