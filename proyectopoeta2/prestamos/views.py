from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Prestamo
from django.urls import reverse_lazy

class PrestamoListView(ListView):
    model = Prestamo
    template_name = 'prestamos/prestamo_list.html'

class PrestamoCreateView(CreateView):
    model = Prestamo
    template_name = 'prestamos/prestamo_form.html'
    fields = ['fecha_prestamo', 'fecha_devolucion', 'estado', 'multa', 'libro', 'cliente', 'estado_devolucion', 'dias_multa']
    success_url = reverse_lazy('prestamo_list')

class PrestamoUpdateView(UpdateView):
    model = Prestamo
    template_name = 'prestamos/prestamo_form.html'
    fields = ['fecha_prestamo', 'fecha_devolucion', 'estado', 'multa', 'libro', 'cliente', 'estado_devolucion', 'dias_multa']
    success_url = reverse_lazy('prestamo_list')

class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = 'prestamos/prestamo_confirm_delete.html'
    success_url = reverse_lazy('prestamo_list')