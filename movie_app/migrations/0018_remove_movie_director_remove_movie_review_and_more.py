# Generated by Django 4.1.1 on 2022-09-24 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0017_remove_review_movie_movie_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='review',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='movie_app.review'),
        ),
    ]