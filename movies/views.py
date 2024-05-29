from rest_framework import viewsets
from .models import Movies
from .serializers import MoviesApi

class MoviesView(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesApi

class AtionMovies(viewsets.ModelViewSet):
    queryset = Movies.objects.filter(typ="action")
    serializer_class = MoviesApi

# Create your views here.
