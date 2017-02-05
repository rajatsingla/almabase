from __future__ import unicode_literals

from django.db import models


class Table8(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=56, blank=True, null=True)
    platform = models.CharField(max_length=16, blank=True, null=True)
    score = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    genre = models.CharField(max_length=17, blank=True, null=True)
    editors_choice = models.CharField(max_length=1, blank=True, null=True)

    def get_genre(self):
        return Table8.objects.values('genre').distinct()

    def get_platform(self):
        return Table8.objects.values('platform').distinct()

    def max_score(self):
        return Table8.objects.latest('score').score

    def search(self,params):
        games=Table8.objects.all()
        if params.get('rank') and params.get('rank')!='':
            games=games.filter(score__gte=int(params.get('rank')))
        if params.get('genre') and params.get('genre')!='':
            games=games.filter(genre=params.get('genre'))
        if params.get('platform') and params.get('platform')!='':
            games=games.filter(platform=params.get('platform'))
        if params.get('choice')!=None and params.get('choice')=="false":
            games=games.filter(editors_choice='N')
        if params.get('choice')!=None and params.get('choice')=="true":
            games=games.filter(editors_choice='Y')
        if params.get('name') and params.get('name')!='':
            games=games.filter(title__icontains=params.get('name'))
        if params.get('order_rank') and params.get('order_rank')=='rank_asc':
            games=games.order_by('score')
        if params.get('order_rank') and params.get('order_rank')=='rank_desc':
            games=games.order_by('score').reverse()
        return games


    class Meta:
        db_table = 'table 8'

# Create your models here.
