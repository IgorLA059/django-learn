from rest_framework import serializers
from .models import Movies

class MoviesApi(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'name', 'duration', 'rating', 'typ']

