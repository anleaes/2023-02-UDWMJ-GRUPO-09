from django.urls import path
from . import views

app_name = 'compras'

urlpatterns = [
    path('', views.list_compras, name='list_compras'),
    path('adicionar/', views.add_compra, name='add_compra'),
    path('editar/<int:id_compra/', views.edit_compra, name='edit_compra'),
    path('excluir/<int:id_compra>/', views.delete_compra, name='delete_compra'),
]
