from django.http import HttpResponse
from django.contrib import admin
from django.urls import path

def index(request):
    return HttpResponse("Halo dunia Django web framework")

def blog(request):
    return HttpResponse("Ini adalah halaman blog")


urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('admin/', admin.site.urls),
]
