from django.urls import path
from . import views

app_name = 'artistas'

urlpatterns = [
    path('', views.list_artistas, name='list_artistas'),
    path('adicionar/', views.add_artista, name='add_artista'),
    path('editar/<int:id_artista/', views.edit_artista, name='edit_artista'),
    path('excluir/<int:id_artista>/', views.delete_artista, name='delete_artista'),
]
