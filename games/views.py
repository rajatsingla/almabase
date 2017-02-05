from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Table8

def index(request):
    game_list = Table8.objects.all()
    template = loader.get_template('games/index.html')
    context = {
        'game_list': game_list,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
