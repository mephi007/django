from django.contrib import admin
from django.urls import path, re_path 

from myapp import views

urlpatterns = [
	path('', views.posts_create),
	path('list', views.posts_list),
	re_path(r'^(?P<id>\d+)/$', views.posts_detail),
	path('list', views.posts_list),
	path('update' , views.posts_update),
	path('delete', views.posts_delete),
]