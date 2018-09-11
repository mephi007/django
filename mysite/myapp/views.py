from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import post
# Create your views here.

def posts_create(requests):
    
    context ={ 
        "title": "create"
    }
    return render(requests, 'index.html', context)

def posts_list(requests):
    queryset= post.objects.all()
    context ={ 
        "object_list": queryset,
        "title": "list"
    }
    return render(requests, 'index.html', context)

def posts_detail(requests, id=None):
    #instance = post.objects.get(id=1)
    instance = get_object_or_404(post, id=id)
    context ={ 
        "title": instance.title,
        "instance": instance,
    }
    return render(requests, 'post_detail.html', context)


# def posts_list(requests):
#     return HttpResponse("<h1>LIST</h1>")

def posts_update(requests):
    return HttpResponse("<h1>UPDATE</h1>")

def posts_delete(requests):
    return HttpResponse("<h1>DELETE</h1>")
