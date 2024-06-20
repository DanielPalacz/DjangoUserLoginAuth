from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {})


def logged_out(request):
    return render(request, "registration/user_logged_out.html", {})


def home(request):
    return render(request, "registration/home.html", {})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})
