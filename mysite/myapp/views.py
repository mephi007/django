from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def posts_home(requests):
    return HttpResponse("<h1>HELLO</h1>")

def posts_create(requests):
    return HttpResponse("<h1>CREATE</h1>")

def posts_detail(requests):
    return HttpResponse("<h1>DETAIL</h1>")

def posts_list(requests):
    return HttpResponse("<h1>LIST</h1>")

def posts_update(requests):
    return HttpResponse("<h1>UPDATE</h1>")

def posts_delete(requests):
    return HttpResponse("<h1>DELETE</h1>")
