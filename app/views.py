from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import *
from django.contrib.auth import *

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully Registered')
                return redirect("/")
        else:
            form = UserCreationForm()
        return render(request, "register.html", {"form":form})
    else:
        return redirect("/profile/")


def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/profile")
                else:
                    messages.warning(request, "Not Logged in successfully! Try Again Later")
                    return redirect("/loggin")
        else:
            form = AuthenticationForm()
        return render(request, 'loggin.html', {"form":form})
    else:
        return redirect("/profile")

def loggout(request):
    logout(request)
    return redirect("/loggin/")

def profile(request):
    if request.user.is_authenticated:
        post_datas = Post.objects.all()
        return render(request, "profile.html", {"post_data":post_datas})
    else:
        return redirect('/loggin/')

@csrf_exempt
def like(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user.is_authenticated:
        if request.user in post.liked.all():
            post.liked.remove(request.user)
            context = {"dislike":False,"postcount":post.liked.all().count()}
        else:
            post.liked.add(request.user)
            context = {"like":True,"postcount":post.liked.all().count()}
    return JsonResponse(context)

def post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                #   print(request.POST)
                form.save()
                messages.success(request, 'Successfully Registered')
                return redirect("/")
        else:
            form = PostForm()
        return render(request, "post_form.html", {"form":form})
    else:
        return redirect("/loggin")


def topic(request):
    if request.user.is_authenticated:
        topics = Topic.objects.all()
        return render(request, 'javatopic.html', {"topics":topics})
    else:
        return redirect("/loggin")

def get_details(request, id):
    if request.user.is_authenticated:
        topics = Topic.objects.all()
        contents = Content.objects.filter(topic=id)
        examples = Example.objects.filter(topic=id)
        return render(request, 'javatopic.html', {"topics":topics, "contents":contents, 'examples':examples})
    else:
        return redirect("/loggin")