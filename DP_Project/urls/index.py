from django.urls import path

from DP_Project.views.index import index
from DP_Project.views.getinfo import getinfo
from DP_Project.views.login import login
from DP_Project.views.logout import logout
from DP_Project.views.register import register

urlpatterns = [
    path('index/', index, name="index"),
    path("getinfo/", getinfo, name="getinfo"),
    path("login/", login, name="login"),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register')
]
