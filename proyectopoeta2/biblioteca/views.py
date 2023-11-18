from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/libro_list.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    
    else:
        form = LibroForm()
    return render(request, 'biblioteca/libro_create.html', {'form': form})

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'biblioteca/libro_detail.html', {'libro': libro})

def modificar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    
    else:
        form = LibroForm(instance=libro)
    
    return render(request, 'biblioteca/libro_edit.html', {'form': form, 'libro': libro})

def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    libro.delete()
    return redirect('listar_libros')