from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

