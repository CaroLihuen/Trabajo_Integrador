from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required,user_passes_test, permission_required
from django.urls import reverse

from compra.models import Producto
from compra.models import Proveedor

# Vistas de productos

def lista_productos(request):
    productos = Producto.objects.all()
    #renderiza la vista de todos los productos
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto_detalle = get_object_or_404(Producto, pk=pk)
    # renderiza detalle de producto
    return render(request, 'productos/detalle_producto.html',{'producto_detalle':producto_detalle})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock_actual')
        Producto.objects.create(nombre=nombre, precio=precio, stock_actual=stock_actual)

        return redirect(reverse('compra:lista_productos'))
    return render(request, 'productos/producto_form.html')

def modificar_producto(request,pk):
    producto = get_object_or_404(Producto,pk=pk)
    if(request.method == 'POST'):
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock_actual')
        producto.nombre = nombre
        producto.precio = precio
        producto.stock_actual = stock_actual
        producto.save()

        return redirect(reverse('compra:lista_productos'))
    
    return render(request, 'productos/producto_form.html', {'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto,pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect(reverse('compra:lista_productos'))
    
    return render (request,'productos/producto_confirm_delete.html', {'producto': producto})

# Vistas de proveedores


def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request,pk):
    proveedor_detalle = get_object_or_404(Proveedor, pk= pk)
    return render(request, 'proveedores/detalle_proveedor.html',{'proveedor_detalle': proveedor_detalle} )

def crear_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        Proveedor.objects.create(nombre=nombre, apellido=apellido, dni=dni)

        return redirect(reverse('compra:lista_proveedores'))
    return render(request, 'proveedores/proveedor_form.html')

def modificar_proveedor(request,pk):
    proveedor = get_object_or_404(Proveedor,pk=pk)
    if(request.method == 'POST'):
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        proveedor.nombre = nombre
        proveedor.apellido = apellido
        proveedor.dni = dni
        proveedor.save()

        return redirect(reverse('compra:lista_proveedores'))
    
    return render(request, 'proveedores/proveedor_form.html', {'proveedor': proveedor})

def eliminar_proveedor(request,pk):
    proveedor = get_object_or_404(Proveedor,pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect(reverse('compra:lista_proveedores'))
    
    return render (request,'proveedores/proveedor_confirm_delete.html', {'proveedor': proveedor})