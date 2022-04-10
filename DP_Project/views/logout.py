# 用户注销
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def logout(request):
    auth.logout(request)
    return redirect("/login")
