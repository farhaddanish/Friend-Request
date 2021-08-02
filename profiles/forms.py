from django import forms
from .models import Profiles
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signupForms (UserCreationForm):
    class Meta:
        model = User
        fields = ["username",'email','password1','password2']



