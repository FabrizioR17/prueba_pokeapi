from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/', views.pokemon_list, name='pokemon_list'),
    path('pokedex/', views.pokedex_list, name='pokedex_list'),
    path('pokemon/<pokemon_identifier>/', views.pokemon_by_id_name, name='pokemon_by_id_name'),
    path('pokedex/<pokedex_identifier>/', views.pokedex_by_id_name, name='pokedex_by_id_name'),
    # path('register/', views.RegisterUserView.as_view(), name='register'),
]
