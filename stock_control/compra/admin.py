from django.contrib import admin
from compra.models import Producto,Proveedor

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    pass
    
