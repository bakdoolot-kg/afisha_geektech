# Generated by Django 4.1.1 on 2022-09-28 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0029_alter_movie_director_alter_movie_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(blank=True, default=datetime.timedelta(days=1), null=True),
        ),
    ]
