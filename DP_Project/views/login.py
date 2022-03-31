from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render


# 用户登录
def login(request):
    if request.method == "GET":
        context = {'previous_page': request.GET.get('from_page', '/index')}
        return render(request, 'login.html', context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect(request.GET.get('from_page', '/index'))
        except:
            context = {'login_info': True, 'previous_page': request.GET.get('from_page', '/index')}
            return render(request, 'login.html', context)
