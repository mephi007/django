from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def posts_home(requests):
	return HttpResponse("<h1>HELLO</h1>")