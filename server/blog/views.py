from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request):
    context = {
        'penulis' : "Komoro"
    }
    return render(request, "blog.html", context)

def cari(request):
    return HttpResponse("ini adalah tampilan pencarian")