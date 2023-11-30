from django.urls import path
from . import views

app_name = 'artistas'

urlpatterns = [
    path('', views.list_artistas, name='list_artistas'),
    path('adicionar/', views.add_arte, name='add_artistas'),
    path('editar/<int:id_artistas/', views.edit_arte, name='edit_artistas'),
    path('excluir/<int:id_artistas>/', views.delete_arte, name='delete_artistas'),
]
