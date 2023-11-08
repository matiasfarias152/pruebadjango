from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('agregar/',views.agregar_cliente, name='agregar_cliente'),
    path('<int:cliente_id>/',views.detalle_cliente,name='detalle_cliente'),
    path('<int:cliente_id>/modificar/',views.modificar_cliente, name='modificar_cliente'),
    path('<int:cliente_id>/eliminar/',views.eliminar_cliente, name='eliminar_cliente'),
]