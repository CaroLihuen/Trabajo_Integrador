from django.contrib import admin
from compra.models import Producto,Proveedor

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock_actual']
    search_fields = ['nombre', 'precio', 'stock_actual']
    pass

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'dni']
    search_fields = ['nombre', 'apellido', 'dni']
    pass
    
