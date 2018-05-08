from rest_framework import serializers
from .models import Games, Quests, Publishers, Developers


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        # fields = ()
        fields = '__all__'


class QuestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quests
        fields = ('game', 'title', 'type')


class PublishersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = 'name'


class DevelopersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developers
        fields = 'name'
