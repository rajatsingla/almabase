from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Table8

def index(request):
    table=Table8()
    genre=table.get_genre()
    platform=table.get_platform()
    max_score=table.max_score()
    context={
        'genre':genre,
        'platform':platform,
        'range':range(0,int(max_score)+1),
        'game_list':table.search(request.GET)
    }
    template = loader.get_template('games/index.html')
    return HttpResponse(template.render(context, request))
