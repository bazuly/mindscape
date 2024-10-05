from django.shortcuts import render


def game_view(request):
    return render(request, "pages/knight_game.html")
