from django.urls import path
from . import views

app_name = 'arte'

urlpatterns = [
    path('', views.list_arte, name='list_arte'),
    path('adicionar/', views.add_arte, name='add_arte'),
    path('editar/<int:id_arte/', views.edit_arte, name='edit_arte'),
    path('excluir/<int:id_arte>/', views.delete_arte, name='delete_arte'),
]

