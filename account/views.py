from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .forms import UserRegistrationForm, StaffUserRegistrationForm, SuperUserRegistrationForm
from .models import CustomUser


def is_superuser(user: CustomUser) -> bool:
    return user.is_authenticated and user.is_superuser


def user_registration(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")

    else:
        form = UserRegistrationForm()

    return render(request, "account/registration/user_registration.html", {"form": form})


@user_passes_test(is_superuser)
def staff_user_registration(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = StaffUserRegistrationForm(request.POST)
        if form.is_valid():
            staff = form.save()
            login(request, staff)
            return redirect("post_list")

    else:
        form = StaffUserRegistrationForm()

    return render(request, "account/registration/staff_user_registration.html", {"form": form})


@user_passes_test(is_superuser)
def super_user_registration(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = SuperUserRegistrationForm(request.POST)
        if form.is_valid():
            super_user = form.save()
            login(request, super_user)
            return redirect("post_list")

    else:
        form = SuperUserRegistrationForm()

    return render(request, "account/registration/super_user_registration.html", {"form": form})
