# -*- coding: utf-8 -*-
from rest_framework import viewsets

from .models import Games, Publishers, Developers, Quests
from .serializers import GamesSerializer


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all().order_by('-title')
    serializer_class = GamesSerializer


class PublishersViewSet(viewsets.ModelViewSet):
    queryset = Publishers.objects.all().order_by('-name')
    serializer_class = GamesSerializer


class DevelopersViewSet(viewsets.ModelViewSet):
    queryset = Developers.objects.all().order_by('-name')
    serializer_class = GamesSerializer


class QuestsViewSet(viewsets.ModelViewSet):
    queryset = Quests.objects.all().order_by('-name')
    serializer_class = GamesSerializer
