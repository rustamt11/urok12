from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def func_one(request):
    return HttpResponse("<h1>POP MUSIC is</h1>")


