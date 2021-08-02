import json
from django import forms
from django.http.response import HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from .forms import signupForms
from django.contrib.auth.decorators import login_required
from .models import Profiles, FriendRequest, SavedNotifaction
from django.contrib import messages
from django.contrib.auth.models import User
from posts.models import Posts
from django.db.models import Q

# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return HttpResponseRedirect('/')
        else:
            messages.success(request, ("login Failed"))
            return HttpResponseRedirect('/login')

    return render(request, 'login.html', {})


def signupUser(request):
    if request.method == 'POST':
        form = signupForms(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

    else:
        form = signupForms()

    return render(request, 'signup.html', {
        'form': form
    })


@login_required
def profiles(request):
    if request.method == 'POST':
        pass
    else:
        profile = Profiles.objects.get(user=request.user)
        posts = Posts.objects.filter(profile=profile)
        return render(request, 'profiles.html', {
            'profile': profile,
            'posts': posts
        })


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/login')


def editProfile(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        bio = request.POST['bio']
        image = request.FILES.get('image')
        profile = Profiles.objects.get(user=request.user)
        user = User.objects.get(username=request.user)
        user.username = username
        user.email = email
        profile.bio = bio
        profile.image = image
        user.save()
        profile.save()

        return HttpResponseRedirect('/')

    else:
        profile = Profiles.objects.get(user=request.user)
    return render(request, 'editProfile.html', {
        'profile': profile
    })


def allUser(request):
    userFriends = Profiles.objects.get(user=request.user)
    count = userFriends.friends.count()
    userFind = []
    if count > 0 :
        for i in userFriends.friends.all():
            userFind.append( Profiles.objects.exclude( user=i).exclude(user=request.user))
            print(userFind)
    else:
        userFind.append( Profiles.objects.exclude(user=request.user))

    
        
    friendRequest = FriendRequest.objects.filter(fromuser=request.user)
    return render(request, 'allUser.html', {
        'userfind': userFind,
        'friendRequest': friendRequest,
        'userFriends' : userFriends
    })


def ajaxMakeFriends(request):
    if request.is_ajax() and request.method == 'POST':
        id = request.POST['id']
        fromuser = request.user
        touser = User.objects.get(id=id)
        firendRequestModel = FriendRequest.objects.filter(
            fromuser=fromuser, touser=touser)
        message = ""
        if len(firendRequestModel) == 0:
            FriendRequest.objects.create(fromuser=fromuser, touser=touser)
            message = True
        else:
            firendRequestModel.delete()
            message = False

        return JsonResponse({
            'message': message
        })


def Notifications(request):
    tosuer = request.user
    friendRequest = FriendRequest.objects.filter(touser=tosuer)
    savedNotifaction = SavedNotifaction.objects.filter(toUser=tosuer)
    return render(request, 'Notifications.html', {
        'filter': friendRequest,
        'savedNotifaction' :savedNotifaction
    })


def acceptFriendRequest(request):
    if request.is_ajax() and request.method == 'POST':
        id = request.POST['id']
        data_user =request.POST.get('data_user')
        fromuser = User.objects.get(id=id)
        savedNotifaction = SavedNotifaction.objects.create(formUser=fromuser,toUser=request.user,accept=True)      
        profile = Profiles.objects.get(user=request.user)
        profile2 = Profiles.objects.get(user=fromuser)
        profile.friends.add(fromuser)
        friendRequest = FriendRequest.objects.get(id=data_user)
        profile2.friends.add(request.user)
        profile.save()
        profile2.save()
        friendRequest.delete()
        savedNotifaction.save()
        return JsonResponse({
            'accepted': True
        })


def deniedFriendRequest(request):
    if request.is_ajax() and request.method == 'POST':
        id = request.POST['id']
        fromuser = User.objects.get(id=id)
        data_user =request.POST.get('data_user')
        savedNotifaction = SavedNotifaction.objects.create(formUser=fromuser,toUser=request.user,denied =True)
        friendRequest = FriendRequest.objects.get(id=data_user)
        savedNotifaction.save()
        friendRequest.delete()

        return JsonResponse({
            'denied': True
        })
