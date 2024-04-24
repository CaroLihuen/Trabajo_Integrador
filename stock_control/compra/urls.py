from django.urls import path
from . import views

app_name = 'compra'

urlpatterns = [
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('detalle_producto/<int:pk>/', views.detalle_producto, name='detalle_productos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('modificar_producto/<int:pk>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar_producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]