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

class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.DateField()

class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.FloatField()
    album = models.ManyToManyField(Album)
    artist = models.ManyToManyField(Artist)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    playlist = models.ManyToManyField(Playlist)