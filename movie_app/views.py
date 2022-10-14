from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DirectorsListSerializer, \
    MoviesListSerializer, \
    ReviewsListSerializer, \
    MoviesReviewSerializer, \
    MovieCreateSerializer, \
    MovieUpdateSerializer, \
    DirectorBaseValidateSerializer, ReviewBaseValidateSerializer
from .serializers import DirectorsListSerializer, MoviesListSerializer, ReviewsListSerializer, MoviesReviewSerializer
from .models import Director, Movie, Review


# Movies
@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        data = MoviesListSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        serializer = MovieCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'message': 'data with errors',
                                  'error': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        movie = Movie.objects.create(
            title=request.data.get("title"),
            description=request.data.get("description"),
            duration=request.data.get("duration"),
            director_id=request.data.get("director"),
        )
        movie.reviews.set(request.data.get("reviews"))
        movie.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Successfully created!'})


@api_view(["GET", "PUT", "DELETE"])
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={"error": "Movie not found"})
    if request.method == 'GET':
        data = MoviesListSerializer(movie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={"message": "Successfully removed!"},
                        status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MovieUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie.title = request.data.get("title")
        movie.description = request.data.get("description")
        movie.duration = request.data.get("duration")
        movie.director_id = request.data.get("director")
        movie.reviews.set(request.data.get("reviews"))
        movie.save()
        return Response(data={'message': 'Successfully updated!',
                              'movie': MoviesListSerializer(movie).data})


# Directors
@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorsListSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = DirectorBaseValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'message': 'data with errors',
                                  'error': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        director = Director.objects.create(
            name=request.data.get('name'),
        )
        director.movies.set(request.data.get('movies'))
        director.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Successfully created!'})


@api_view(['GET', 'PUT', 'DELETE'])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={"error": "Director not found"})
    if request.method == 'GET':
        data = DirectorsListSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(data={'message': 'Successfully removed!'},
                        status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = DirectorBaseValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        director.name = request.data.get('name')
        director.movies.set(request.data.get('movies'))
        director.save()
        return Response(data={'message': 'Successfully updated!',
                              'director': DirectorsListSerializer(director).data})


# Reviews
@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewsListSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewBaseValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'message': 'review data with error',
                                  'error': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        review = Review.objects.create(
            text=request.data.get('text'),
            stars=request.data.get('stars')
        )
        review.save()
        return Response(status=status.HTTP_201_CREATED,
                        data={'message': 'Successfully created!'})


@api_view(['GET', 'PUT', 'DELETE'])
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={"error": "Review not found"})
    if request.method == 'GET':
        data = ReviewsListSerializer(review).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(data={'message': 'Successfully removed!'},
                        status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ReviewBaseValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data={'message': 'Successfully updated!',
                              'review': ReviewsListSerializer(review).data})


@api_view(["GET"])
def movie_reviews_view(request):
    movies = Movie.objects.all()
    data = MoviesReviewSerializer(movies, many=True).data
    return Response(data=data)
