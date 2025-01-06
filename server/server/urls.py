from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from .views import index, blog



from kontak import views as tampilanViews 

urlpatterns = [
    path('', index),
    path('blog/', include('blog.urls') ),
    path('admin/', admin.site.urls),
    path('kontak/', tampilanViews.index),
]
