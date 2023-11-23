from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegistrationForm, StaffUserRegistrationForm, SuperUserRegistrationForm


