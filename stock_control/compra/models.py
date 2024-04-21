from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    dni = models.CharField(max_length=8, unique=True)
    pass
    
    class Meta:
        ordering = ('nombre', 'apellido',)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - dni: {self.dni}'

   

class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    precio = models.IntegerField(max_length=20)
    stock_actual = models.IntegerField(min=1, max_length=20)
    proveedor = models.ManyToOneRel(Proveedor, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('nombre','proovedor', 'stock')

    def __str__(self):
        return f'Producto: {self.nombre}, precio: {self.precio}, stock actual: {self.stock_actual}, proveedor: {self.proveedor}'