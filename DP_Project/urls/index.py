from django.urls import path

from DP_Project.views.index import index
from DP_Project.views.getinfo import getinfo

urlpatterns = [
    path('', index, name="index"),
    path("getinfo/", getinfo, name="getinfo"),
]