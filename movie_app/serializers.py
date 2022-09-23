from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class MoviesListSerializer(serializers.ModelSerializer):
    director = DirectorsListSerializer(instance=Movie, data="name")

    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class ReviewsListSerializer(serializers.ModelSerializer):
    movie = MoviesListSerializer(instance=Review, data=Movie)

    class Meta:
        model = Review
        fields = "id text movie".split()
