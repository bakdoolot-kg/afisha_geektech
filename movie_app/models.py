from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(max_length=300)
    movie = models.ForeignKey("Movie", related_name="movie", on_delete=models.CASCADE)


class Movie(models.Model):
    title = models.CharField(max_length=255, )
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField(null=True)
    director = models.ForeignKey("Director", null=True, blank=True, related_name="director", on_delete=models.CASCADE)
    # director = models.ManyToManyField("Director", related_name="director")
    # director = models.ManyToManyField("Director")

    def __str__(self):
        return self.title
