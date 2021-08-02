from posts.models import Posts
from django.shortcuts import render
from .forms import createPostForms
from profiles.models import Profiles
from django.http import HttpResponseRedirect
# Create your views here.




def createPost (request):
    if request.method == "POST":
        text = request.POST.get("text")
        profile = Profiles.objects.get(user=request.user)
        posts = Posts.objects.create(text=text,profile=profile)
        posts.save()
        

        
        return HttpResponseRedirect("/")

    

    return render(request,"createPost.html" ,{
        
    })