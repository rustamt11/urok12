from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def miles(request):
    return HttpResponse("<h1>MILES Davis ... is</h1>")

def duke(request):
    return HttpResponse("<h1>Duke Ellington ... is</h1>")

def john(request):
    return HttpResponse("<h1>John Coltrane ... is</h1>")

def charlie(request):
    return HttpResponse("<h1>Charlie Parker ... is</h1>")

def lst_genres_jazz(request):
    return render(request, "genres.html")

def main_page(request):
    return render(request, "index.html")
