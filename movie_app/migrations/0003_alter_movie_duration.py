# Generated by Django 4.1.1 on 2022-09-22 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_remove_movie_director_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(null=True),
        ),
    ]
