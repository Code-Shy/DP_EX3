from django.urls import path

from DP_Project.views import scatter, Greedy
from DP_Project.views.Backtrack import Backtrack
from DP_Project.views.Dynamic import Dynamic
from DP_Project.views.ga import ga
from DP_Project.views.Greedy import Greedy
from DP_Project.views.index import index
from DP_Project.views.login import login
from DP_Project.views.logout import logout
from DP_Project.views.register import register

urlpatterns = [
    path('index/', index, name="index"),
    path('login/', login, name="login"),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('BackTrace/', Backtrack, name="BackTrace"),
    path("Dynamic/", Dynamic, name="Dynamic"),
    path("ga/", ga, name="ga"),
    path('Greedy/', Greedy, name='Greedy'),
]
