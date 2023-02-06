from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/', views.pokemon_list, name='pokemon_list'),
    path('pokedex/', views.pokedex_list, name='pokedex_list'),
    path('pokemon/<pokemon_id>/', views.pokemon_by_id, name='pokemon_by_id'),
]
