from django.shortcuts import render, get_object_or_404, redirect
from .models import Prestamo
from .forms import PrestamoForm
from datetime import date
from datetime import datetime

def calcular_dias_multa(fecha_devolucion):
    hoy = datetime.now().date()

    print(f"Fecha de devolución: {fecha_devolucion}")
    print(f"Fecha de hoy: {hoy}")

    if fecha_devolucion:
        # Convierte la fecha de devolución a objeto date si no lo es
        if isinstance(fecha_devolucion, datetime):
            fecha_devolucion = fecha_devolucion.date()

        if fecha_devolucion < hoy:
            dias_multa = (hoy - fecha_devolucion).days
            print(f"dias de multa: {dias_multa}")
            return dias_multa
        else:
            print("ta a futuro")
            return 0  
    else:
        print("no fecha devolucion")
        return 0 

def listar_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos/prestamo_list.html', {'prestamos': prestamos})

def agregar_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)

            # deshabilitar checkbox estado
            prestamo.estado_devolucion = False
            prestamo.save()

            # actualizar dias de multa
            dias_multa = calcular_dias_multa(prestamo.fecha_devolucion)
            prestamo.dias_multa = dias_multa
            prestamo.save()

            return redirect('listar_prestamos')
    else:
        form = PrestamoForm()

    return render(request, 'prestamos/prestamo_create.html', {'form': form})

def detalle_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    dias_multa = calcular_dias_multa(prestamo.fecha_devolucion)
    return render(request, 'prestamos/prestamo_detail.html', {'prestamo': prestamo, 'dias_multa':dias_multa})

def modificar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == "POST":
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamos')
    
    else:
        form = PrestamoForm(instance=prestamo)
    
    return render(request, 'prestamos/prestamo_edit.html', {'form': form, 'prestamo': prestamo})

def eliminar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    prestamo.delete()
    return redirect('listar_prestamos')