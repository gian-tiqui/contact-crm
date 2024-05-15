from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
  class Meta:
    model=User
    fields=['username', 'password', 'password2']


class AddContactForm(ModelForm):
  class Meta:
    model=Contact
    fields="__all__"
