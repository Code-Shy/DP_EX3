# 用户注销
from django.contrib import auth
from django.http import HttpResponseRedirect


def logout(request):
    auth.logout(request)
    print('-----------------------------')
    print(request.GET.get('from_page'))
    print(request.GET.get('/logout'))

    print('-----------------------------')
    return HttpResponseRedirect(request.GET.get('from_page', '/logout'))
