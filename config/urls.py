from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from config.views import index
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('users/', include('users.urls')),
    path('fridge/', include('fridge.urls')),
]