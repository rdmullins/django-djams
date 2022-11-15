from django.db import models

# Create your models here.
class Playlist(models.Model):
    title = models.CharField(max_length=100)

class Genre(models.Model):
    genre = models.CharField(max_length=100)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=500)
    bio = models.TextField()

