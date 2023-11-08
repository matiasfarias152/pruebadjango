from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'clientes/listar_clientes.html',{'clientes':clientes})


def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    
    else:
        form = ClienteForm()
    return render(request,'clientes/agregar_cliente.html',{'form':form})


def detalle_cliente(request,cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request,'clientes/detalle_cliente.html',{'cliente':cliente})


def modificar_cliente(request,cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request,'clientes/modificar_cliente.html',{'form':form,'cliente':cliente})

def eliminar_cliente(request,cliente_id):
    cliente = get_object_or_404(Cliente,pk=cliente_id)
    cliente.delete()
    return redirect('listar_clientes')


