from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorsListSerializer, MoviesListSerializer, ReviewsListSerializer
from .models import Director, Movie, Review


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    data = DirectorsListSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    data = MoviesListSerializer(movies, many=True).data
    return Response(data=data)


@api_view(["GET"])
def reviews_view(request):
    reviews = Review.objects.all()
    data = ReviewsListSerializer(reviews, many=True).data
    return Response(data=data)