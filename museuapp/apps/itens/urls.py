from django.urls import path
from . import views

app_name = 'itens'

urlpatterns = [
    path('', views.list_itens, name='list_itens'),
    path('adicionar/', views.add_item, name='add_item'),
    path('editar/<int:id_item/', views.edit_item, name='edit_item'),
    path('excluir/<int:id_item>/', views.delete_item, name='delete_item'),
    
]

