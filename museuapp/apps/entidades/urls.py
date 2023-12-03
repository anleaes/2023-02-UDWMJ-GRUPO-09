from django.urls import path
from . import views

app_name = 'entidades'

urlpatterns = [
    path('', views.list_entidades, name='list_entidades'),
    path('adicionar/', views.add_entidade, name='add_entidade'),
    path('editar/<int:id_entidade/', views.edit_entidade, name='edit_entidade'),
    path('excluir/<int:id_entidade>/', views.delete_entidade, name='delete_entidade'),
]
