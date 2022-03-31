from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


# 用户注册
def register(request):
    if request.method == "GET":
        context = {'previous_page': request.GET.get('from_page', '/index')}
        return render(request, 'register.html', context)
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            # 判断用户名是否存在
            if User.objects.filter(username=username).exists():
                context = {'register_info': True, 'previous_page': request.GET.get('from_page', '/index')}
                return render(request, 'register.html', context)
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return HttpResponseRedirect(request.GET.get('from_page', '/index'))
        except:
            return HttpResponse('注册过程异常，请重新注册！')
