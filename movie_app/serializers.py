from django.db.models.functions import Round
from django.db.models import Avg
from rest_framework import serializers
from .models import Director, Movie, Review


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


class ReviewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class MoviesListSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()

    @staticmethod
    def get_director(obj_movie):
        return obj_movie.director.name


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
