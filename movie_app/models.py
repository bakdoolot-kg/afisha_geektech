from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Director(models.Model):
    name = models.CharField(max_length=255, null=True)
    movies = models.ManyToManyField("Movie", blank=True, null=True, related_name="director_movies")

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(max_length=300)
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)

    def __str__(self):
        return self.text


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(null=True)
    reviews = models.ManyToManyField("Review", blank=True, null=True)
    director = models.ForeignKey("Director", on_delete=models.CASCADE, blank=True, null=True, related_name="director_movie")

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        try:
            return self.director.name
        except Director:
            return ""