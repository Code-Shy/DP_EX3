from django.urls import path

from DP_Project.views.index import index

urlpatterns = [
    path('', index, name="index"),
]