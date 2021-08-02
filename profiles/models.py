
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Profiles (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=50,blank=True)
    image = models.ImageField(upload_to="media",default="media/default.png")
    friends = models.ManyToManyField(User,related_name="friends",blank=True)


    def __str__(self):
        return f" UserName :    {self.user}"



class FriendRequest (models.Model):
    fromuser = models.ForeignKey(User,on_delete= models.CASCADE,related_name="fromuser")
    touser =  models.ForeignKey(User,on_delete= models.CASCADE,related_name="touser")




class SavedNotifaction (models.Model):
    formUser = models.ForeignKey(User,on_delete=models.CASCADE,related_name="fromUser")
    toUser =  models.ForeignKey(User,on_delete= models.CASCADE,related_name="toUser",null=True)
    accept = models.BooleanField(blank=True,null=True)
    denied = models.BooleanField(blank=True,null=True)
    time = models.DateField(auto_now=True)
