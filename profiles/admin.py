from django.contrib import admin
from .models import Profiles,FriendRequest,SavedNotifaction
# Register your models here.



admin.site.register(Profiles)
admin.site.register(FriendRequest)
admin.site.register(SavedNotifaction)
