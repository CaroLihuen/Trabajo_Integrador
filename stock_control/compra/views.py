from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required,user_passes_test, permission_required
from django.urls import reverse

from compra.models import Producto

# Vistas de productos

def lista_productos(request):
    productos = Producto.objects.all()
    #renderiza la vista de todos los productos
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_productos(request, pk):
    producto_detalle = get_object_or_404(Producto, pk=pk)
    # renderiza detalle de producto
    return render(request, 'productos/detalle_producto.html',{'producto_detalle':producto_detalle})

def crear_producto(request):
    if request.method == 'Post':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock_actual')
        Producto.objects.create(nombre=nombre, precio=precio, stock_actual=stock_actual)

        return redirect(reverse('productos: lista_productos'))
    return render(request, 'productos/producto_form.html')

def modificar_producto(request,pk):
    producto = get_object_or_404(Producto,pk=pk)
    if(request.method == 'PUT'):
        nombre = request.PUT.get('nombre')
        precio = request.PUT.get('precio')
        stock_actual = request.PUT.get('stock_actual')
        producto.nombre = nombre
        producto.precio = precio
        producto.stock_actual = stock_actual
        producto.save()

        return redirect(reverse('productos: lista_productos'))
    
    return render(request, 'productos/producto_form.html', {'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto,pk=pk)
    if request.method == 'DELETE':
        producto.delete()
        return redirect(reverse('productos: lista_productos'))
    
    return render (request,'productos/producto_confirm_delete.html', {'producto': producto})

