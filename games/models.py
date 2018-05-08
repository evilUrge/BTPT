# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models


class Publishers(models.Model):
    name = models.TextField(unique=True, blank=False)


class Developers(models.Model):
    name = models.TextField(unique=True, blank=False)


class Games(models.Model):
    YEAR_CHOICES = [(r, r) for r in range(1970, datetime.date.today().year + 1)]
    DEFAULT_YEAR_NOW = datetime.datetime.now().year

    title = models.TextField(unique=True)
    developers = models.ForeignKey(Developers, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    year = models.IntegerField(choices=YEAR_CHOICES, default=DEFAULT_YEAR_NOW)


class Quests(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    title = models.TextField(unique=False)
    type = models.CharField(max_length=1, choices=(('M', 'MAIN'), ('S', 'SIDE')), default='M')
