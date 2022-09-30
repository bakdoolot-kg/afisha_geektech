# Generated by Django 4.1.1 on 2022-09-28 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0038_alter_director_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director_movie', to='movie_app.director'),
        ),
    ]
