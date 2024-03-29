# Generated by Django 4.2.5 on 2023-10-31 12:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('release_year', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='movie_images/%Y/%m/%d')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films.category')),
            ],
        ),
    ]
