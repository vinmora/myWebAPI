from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request):
    return render(request, "blog.html")

def cari(request):
    return HttpResponse("ini adalah tampilan pencarian")