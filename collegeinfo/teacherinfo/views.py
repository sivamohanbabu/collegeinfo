<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import TeacherProfile

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            TeacherProfile.objects.create(
                user=user,
                department=form.cleaned_data["department"],
                phone=form.cleaned_data["phone"]
            )
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "teacherinfo/login.html",
                          {"error": "Invalid credentials"})

    return render(request, "login.html")


@login_required
def dashboard(request):
    profile = TeacherProfile.objects.get(user=request.user)
    return render(request, "dashboard.html", {"profile": profile})


def logout_view(request):
    logout(request)
    return redirect("login")
=======
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def landing(request):
    return render(request,"landing.html")
def register(request):
    return render(request,'register.html')
def registerinfo(request):
    if request.method == "POST":
        data = {
            "name" : request.POST.get("name"),
            "email": request.POST.get("email"),
            "date":request.POST.get("date")
        }
        # jsondata = JsonResponse(data)
    return render(request,'registerinfo.html',data)
     

>>>>>>> fee0cb37955689d03c653e0254ac5c711a175691
