from django.contrib import admin
from django.urls import path, re_path 

from myapp import views

urlpatterns = [
	path('', views.posts_home),
	path('create', views.posts_create),
	path('detail', views.posts_detail),
	path('list', views.posts_list),
	path('update' , views.posts_update),
	path('delete', views.posts_delete),
]