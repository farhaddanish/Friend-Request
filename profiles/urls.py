from django.urls import path
from . import views



urlpatterns = [
    path('login/',views.loginUser ,name="login"),
    path('logout/',views.logoutUser ,name="logout"),
    path('editProfile/',views.editProfile ,name="editProfile"),
    path('signup/',views.signupUser ,name="signup"),
    path('',views.profiles ,name="profiles"),
    path('allUser',views.allUser ,name="allUser"),
    path('Notifications',views.Notifications ,name="Notifications"),


    # aajax
    path('ajaxMakefriends',views.ajaxMakeFriends ,name="ajaxMakeFriends"),
    path('acceptFriendRequest/',views.acceptFriendRequest ,name="acceptFriendRequest"),
    path('deniedFriendRequest/',views.deniedFriendRequest ,name="deniedFriendRequest"),






]
