from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy
from .models import post
from .form import PostForm
# Create your views here.

def posts_form(requests):
    form = PostForm(requests.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    # if requests.method == 'POST':
    #     print("title " + requests.POST.get("content"))
    #     print(requests.POST.get("title"))
    #     #post.object.create(title=title)
    context = {
    "form": form,
    }
    return render(requests, 'post_form.html', context)

def posts_create(requests):
    form = PostForm()
    if requests.method == 'POST':
        print(requests.POST)
    context = {
    "form": form,
    }
    return render(requests, 'post_form.html', context)

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
