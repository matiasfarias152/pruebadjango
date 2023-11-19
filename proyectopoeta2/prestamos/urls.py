from django.urls import path
from . import views

urlpatterns = [
    path('prestamos/', views.listar_prestamos, name='listar_prestamos'),
    path('prestamos/agregar/', views.agregar_prestamo, name='agregar_prestamo'),
    path('prestamos/<int:prestamo_id>/', views.detalle_prestamo, name='detalle_prestamo'),
    path('prestamos/<int:prestamo_id>/editar/', views.modificar_prestamo, name='modificar_prestamo'),
    path('prestamos/<int:prestamo_id>/eliminar/', views.eliminar_prestamo, name='eliminar_prestamo'),
]