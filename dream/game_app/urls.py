from django.urls import path
from .views import game_view

app_name = "game_app"


urlpatterns = [
    path('knight_game/', game_view, name='game_app')
]
