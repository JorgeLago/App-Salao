from main.views import clientes
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', clientes,)
]
