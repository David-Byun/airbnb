# Generated by Django 2.2.5 on 2021-07-10 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0004_auto_20210710_2053'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='accuracy',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='check_in',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='cleanliness',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='communication',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='location',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='room',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='rooms.Room'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='value',
            field=models.IntegerField(default=5),
        ),
    ]