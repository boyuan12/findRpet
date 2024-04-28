from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        phone = request.POST["phone_number"]


        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        p =  Profile.objects.create(user=user, phone_number=phone)
        p.save()

        login(request, user)

        return redirect("/")
    else:
        return render(request, "authentication/register.html")
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is None:
            print("INVALID LOGIN INFO")
            messages.add_message(request, messages.ERROR, "Username and/or password is incorrect :(")
            return render(request, "authentication/login.html")
            
        login(request, user)

        return redirect("/")
    else:
        return render(request, "authentication/login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


def register_pa(request):
    return render(request, "authentication/pa_register.html")