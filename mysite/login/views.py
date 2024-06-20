from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {})


def logged_out(request):
    return render(request, "registration/user_logged_out.html", {})


def home(request):
    return render(request, "registration/home.html", {})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})
