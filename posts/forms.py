from django import forms
from django.db import models
from django.forms import fields
from.models import Posts


class createPostForms(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ["text","profile"]
