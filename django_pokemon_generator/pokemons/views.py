from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

# Create your views here.

def index(request):
    all_pokemon = Pokemon.objects.all()
    context = {
        "all_pokemon": all_pokemon
    }
    return render(request, 'pokemons/index.html', context)