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
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    year = models.DateField()

class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.FloatField()
    album = models.ManyToManyField(Album, related_name="track_list")
    artist = models.ManyToManyField(Artist, related_name="artist_list")
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="genre_list")
    playlist = models.ManyToManyField(Playlist, related_name="playlist_list")