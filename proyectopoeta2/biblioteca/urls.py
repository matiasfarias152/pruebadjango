from django.urls import path
from .views import LibroListView, LibroCreateView, LibroUpdateView, LibroDeleteView

urlpatterns = [
    path('libros/', LibroListView.as_view(), name='libro_list'),
    path('libros/nuevo/', LibroCreateView.as_view(), name='libro_create'),
    path('libros/editar/<int:pk>/', LibroUpdateView.as_view(), name='libro_edit'),
    path('libros/eliminar/<int:pk>/', LibroDeleteView.as_view(), name='libro_delete'),
]