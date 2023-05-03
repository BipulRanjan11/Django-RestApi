from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Artist, Work


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


class WorkSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)

    class Meta:
        model = Work
        fields = ['id', 'link', 'work_type', 'artist']


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)
