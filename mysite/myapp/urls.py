from django.contrib import admin
from django.urls import path, re_path 

from myapp import views

urlpatterns = [

	path('', views.posts_home),
]