
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('biblioteca/', include('biblioteca.urls')),
    path('prestamos/', include('prestamos.urls')),  # Esta línea es suficiente, asegúrate de no tener otra similar.
    path('', include('clientes.urls')),  # Si quieres redirigir a clientes al ingresar la raíz.
]