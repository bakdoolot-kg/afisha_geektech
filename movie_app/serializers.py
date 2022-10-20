from django.db.models.functions import Round
from django.db.models import Avg
from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


# DIRECTOR SERIALIZERS
class DirectorBaseValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=255)
    movies = serializers.ListField(min_length=1)

    def validate_movies(self, movies):
        movies_from_db = Movie.objects.filter(id__in=movies)
        if len(movies) != movies_from_db.count():
            raise ValidationError('Movie Not Found')
        return movies


class MovieTitleToDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title'.split()


class DirectorsListSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = "id name movies_count".split()

    @staticmethod
    def get_movies_count(obj):
        return len([{"id": movie.id, "title": movie.title} for movie in obj.movies.all()])


# REVIEW SERIALIZERS
class ReviewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewBaseValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=3, max_length=300)
    stars = serializers.IntegerField(min_value=1, max_value=5)


# MOVIE SERIALIZERS
class MoviesListSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()

    @staticmethod
    def get_director(obj_movie):
        return obj_movie.director.name


class MovieCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class MoviesReviewSerializer(serializers.ModelSerializer):
    # reviews = ReviewsListSerializer(many=True)
    reviews_list = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title reviews_list rating'.split()

    @staticmethod
    def get_reviews_list(obj_movie):
        return [[{"text": review.text, "rate": review.stars}] for review in obj_movie.reviews.all()]

    def get_rating(self, obj):
        return obj.reviews.aggregate(rating=Round(Avg("stars")))['rating']


class MovieBaseValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=20)
    description = serializers.CharField(required=False, default="Description is empty")
    duration = serializers.DurationField(required=False)
    director = serializers.IntegerField()
    reviews = serializers.ListField(child=serializers.IntegerField(min_value=1), required=False)

    def validate_director(self, director):
        try:
            Director.objects.get(id=director)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with id={director} Not Found')
        return director

    def validate_reviews(self, reviews):
        reviews_from_db = Review.objects.filter(id__in=reviews)
        if len(reviews) != reviews_from_db.count():
            raise ValidationError('Review not found!')
        return reviews


class MovieCreateSerializer(MovieBaseValidateSerializer):
    def validate_title(self, title):
        if Movie.objects.filter(title=title):
            raise ValidationError('Title must be unique')
        return title


class MovieUpdateSerializer(MovieBaseValidateSerializer):
    pass
