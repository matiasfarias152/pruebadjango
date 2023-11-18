from django.urls import path
from . import views



urlpatterns = [
    path('libros/', views.listar_libros, name='listar_libros'),
    path('libros/agregar/', views.agregar_libro, name='agregar_libro'),
    path('libros/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('libros/<int:libro_id>/editar/', views.modificar_libro, name='modificar_libro'),
    path('libros/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]