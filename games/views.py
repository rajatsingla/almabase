from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Table8

def index(request):
    table=Table8()
    genre=table.get_genre()
    platform=table.get_platform()
    max_score=table.max_score()
    games,page_range=table.search(request.GET)
    context={
        'genre':genre,
        'platform':platform,
        'range':range(0,int(max_score)+1),
        'game_list':games,
        'page_range':page_range,
        'rank': request.GET.get('rank'),
        'genres': request.GET.get('genre'),
        's_platform': request.GET.get('platform'),
        'order_rank': request.GET.get('order_rank'),
        'choice_t': request.GET.get('choice')=="true",
        'choice_f': request.GET.get('choice')=="false",
    }
    if request.GET.get('name') and request.GET.get('name')!=None:
        context['name']=request.GET.get('name')
    template = loader.get_template('games/index.html')
    response=HttpResponse(template.render(context, request))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, PUT"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    return response
