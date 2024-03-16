# Generated by Django 4.2.5 on 2024-01-21 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0007_remove_movie_cat_movie_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviecomment',
            name='person',
        ),
        migrations.AddField(
            model_name='moviecomment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]