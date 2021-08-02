from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profiles
# Create your models here.



class Posts (models.Model):
    text = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE,default="",null=True,blank=True)

    def __str__(self):
        return f' Profiles :     {self.profile}'
