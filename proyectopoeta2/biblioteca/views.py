
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Libro
from django.urls import reverse_lazy

class LibroListView(ListView):
    model = Libro
    template_name = 'biblioteca/libro_list.html'

class LibroCreateView(CreateView):
    model = Libro
    template_name = 'biblioteca/libro_form.html'
    fields = ['titulo', 'autor', 'fecha', 'cantidad_total', 'genero']
    success_url = reverse_lazy('libro_list')

class LibroUpdateView(UpdateView):
    model = Libro
    template_name = 'biblioteca/libro_form.html'
    fields = ['titulo', 'autor', 'fecha', 'cantidad_total', 'genero']
    success_url = reverse_lazy('libro_list')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'biblioteca/libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')