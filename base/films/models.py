from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.db import models
from django.utils import timezone
from slugify import slugify

class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField()
    release_year = models.IntegerField()
    image = models.ImageField(upload_to='movie_images/%Y/%m/%d')
    date_added = models.DateTimeField(default=timezone.now)
    cat = models.ForeignKey('Category', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_film', kwargs={'film_slug': self.slug})

@receiver(pre_save, sender=Movie)
def create_movie_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_movies', kwargs={'category_slug': self.slug})


class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user} on {self.movie.title}"

    class Meta:
        ordering = ['-created_at']

