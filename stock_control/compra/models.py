from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    pass
    
    class Meta:
        ordering = ('nombre', 'apellido',)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - dni: {self.dni}'

   

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, null=True)
    
    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return f'Producto: {self.nombre}, precio: {self.precio}, stock actual: {self.stock_actual}, proveedor: {self.proveedor}'