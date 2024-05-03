from django import forms
from django.forms import ValidationError
from compra.models import Proveedor,Producto

# Form de Proveedor
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields= [
            'nombre','apellido','dni'
        ]

    def clean_nombre(self):
       nombre = self.cleaned_data.get('nombre')
       if len(nombre) < 4 :
          raise ValidationError(f'La propiedad nombre debe tener al menos 4 letras.')
       if isinstance(nombre,int):
           raise ValidationError(f'La propiedad nombre debe ser un string.')
       return nombre
    
    def clean_apellido(self):
       apellido = self.cleaned_data.get('apellido')
       if len(apellido) < 4 :
          raise ValidationError(f'La propiedad apellido debe tener al menos 4 letras.')
       if isinstance(apellido,int) :
           raise ValidationError(f'La propiedad apellido debe ser un string.')
       return apellido
    
    def clean_dni(self):
       dni = self.cleaned_data.get('dni')
       if len(dni) < 8 :
          raise ValidationError(f'La propiedad dni debe tener al menos 8 dígitos.')
       if isinstance(dni,float):
           raise ValidationError(f'La propiedad dni debe ser un número.')
       return dni
    

# Form de Producto 
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields= [
            'nombre','precio','stock_actual','proveedor'
        ]

    def clean_nombre(self):
       nombre = self.cleaned_data.get('nombre')
       if len(nombre) < 4 :
          raise ValidationError(f'La propiedad nombre debe tener al menos 4 letras.')
       if isinstance(nombre,int):
           raise ValidationError(f'La propiedad nombre debe ser un string.')
       return nombre
    
    def clean_precio(self):
       precio = self.cleaned_data.get('precio')
       if isinstance(precio,int):
           raise ValidationError(f'La propiedad precio debe ser un string.')
       return precio
    
    def clean_stock_actual(self):
       stock_actual = self.cleaned_data.get('stock_actual')
       if isinstance(stock_actual,str):
           raise ValidationError(f'La propiedad stock_actual debe ser un número.')
       return stock_actual