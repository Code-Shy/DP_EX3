from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# 用户登录
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    username = request.POST['username']
    password = request.POST['password']
    print(username)
    try:
        user = authenticate(request, username=username, password=password)
        auth.login(request, user)
        return redirect("/index/")
    except:
        return render(request, 'login.html')
