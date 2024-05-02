from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.urls import reverse

from compra.models import Producto
from compra.models import Proveedor
from compra.forms import ProductoForm
from compra.forms import ProveedorForm

# Vistas de productos

def lista_productos(request):
    productos = Producto.objects.all()
    #renderiza la vista de todos los productos
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto_detalle = get_object_or_404(Producto, pk=pk)
    # renderiza detalle de producto
    return render(request, 'productos/detalle_producto.html',{'producto_detalle':producto_detalle})

@permission_required('compra.crear_producto', raise_exception=True)
def crear_producto(request):
    if (request.method == 'POST'):
        producto_form = ProductoForm(request.POST) 
        if(producto_form.is_valid()):
            nuevo_producto = producto_form.save(commit=True)
            messages.success(request, 'Se ha agregado el nuevo producto')
            return redirect(reverse('compra:detalle_producto', args={nuevo_producto.id}))
    else:
        producto_form = ProductoForm()

    return render(request, 'productos/producto_form.html', {'form': producto_form})

def modificar_producto(request,pk):
    producto = get_object_or_404(Producto,pk=pk)
    if (request.method == 'POST'):
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock_actual')
        producto.nombre = nombre
        producto.precio = precio
        producto.stock_actual = stock_actual
        producto.save()

        return redirect(reverse('compra:lista_productos'))
    
    return render(request, 'productos/producto_modificado.html', {'producto': producto})

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

@permission_required('compra.crear_proveedor', raise_exception=True)
def crear_proveedor(request):
    if (request.method == 'POST'):
        proveedor_form = ProveedorForm(request.POST)
        if(proveedor_form.is_valid()):
            nuevo_proveedor = proveedor_form.save(commit=True)
            messages.success(request, 'Se ha agregado un nuevo proveedor')
            return redirect(reverse('compra:detalle_proveedor', args={nuevo_proveedor.id}))
    else:
        proveedor_form = ProveedorForm()

    return render(request, 'proveedores/proveedor_form.html', {'forms': proveedor_form})

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
    
    return render(request, 'proveedores/proveedor_modificado.html', {'proveedor': proveedor})

def eliminar_proveedor(request,pk):
    proveedor = get_object_or_404(Proveedor,pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect(reverse('compra:lista_proveedores'))
    
    return render (request,'proveedores/proveedor_confirm_delete.html', {'proveedor': proveedor})