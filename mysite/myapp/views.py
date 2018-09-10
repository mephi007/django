from django.shortcuts import render
from django.http import HttpResponse
from .models import post
# Create your views here.


def posts_home(requests):
    context ={ 
        "title": "home"
    }
    return render(requests, 'index.html', context)

def posts_create(requests):
    queryset= post.objects.all()
    context ={ 
        "object_list": queryset,
        "title": "create"
    }
    return render(requests, 'index.html', context)

def posts_detail(requests):
    return HttpResponse("<h1>DETAIL</h1>")

def posts_list(requests):
    return HttpResponse("<h1>LIST</h1>")

def posts_update(requests):
    return HttpResponse("<h1>UPDATE</h1>")

def posts_delete(requests):
    return HttpResponse("<h1>DELETE</h1>")
