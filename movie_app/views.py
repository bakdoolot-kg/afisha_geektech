from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorsListSerializer, MoviesListSerializer, ReviewsListSerializer, MoviesReviewSerializer
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
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Movie not found"})
    data = MoviesListSerializer(movie).data
    return Response(data=data)


@api_view(["GET"])
def reviews_view(request):
    reviews = Review.objects.all()
    data = ReviewsListSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(["GET"])
def movie_reviews_view(request):
    movies = Movie.objects.all()
    data = MoviesReviewSerializer(movies, many=True).data
    return Response(data=data)


@api_view(["GET"])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Director not found"})
    data = DirectorsListSerializer(director).data
    return Response(data=data)


@api_view(["GET"])
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Review not found"})
    data = ReviewsListSerializer(review).data
    return Response(data=data)