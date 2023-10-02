from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def param_func(request, param):
    return HttpResponse(f"<h1>{param}</h1>")


def handler_404(request, exception):
    return HttpResponse(f"<h1>404 UKAJONIM SUR BOTTAN</h1>")