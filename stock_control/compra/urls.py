from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'compra'  

#urls del entorno de compra
urlpatterns = [
    path('', TemplateView.as_view(template_name='base/compra.html'), name='compra'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('detalle_producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('modificar_producto/<int:pk>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar_producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('lista_proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('detalle_proveedor/<int:pk>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),
    path('modificar_proveedor/<int:pk>/', views.modificar_proveedor, name='modificar_proveedor'),
    path('eliminar_proveedor/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
]