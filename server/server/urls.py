from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from .views import index, blog
from blog import views as tampilanBlog

urlpatterns = [
    path('', index),
    path('blog/', tampilanBlog.index),
    path('admin/', admin.site.urls),
]
