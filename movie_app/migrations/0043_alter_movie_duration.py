# Generated by Django 4.1.1 on 2022-09-28 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0042_alter_movie_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(days=365), null=True),
        ),
    ]