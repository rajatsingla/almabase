from __future__ import unicode_literals

from django.db import models


class Table8(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=56, blank=True, null=True)
    platform = models.CharField(max_length=16, blank=True, null=True)
    score = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    genre = models.CharField(max_length=17, blank=True, null=True)
    editors_choice = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'table 8'

# Create your models here.
