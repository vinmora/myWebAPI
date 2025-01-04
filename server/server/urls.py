from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from .views import index, blog

urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('admin/', admin.site.urls),
]
