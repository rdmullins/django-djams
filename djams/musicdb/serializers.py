from rest_framework import serializers
from .models import *

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

class SongViewSetSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)
    album = AlbumSerializer(many=True)
    genre = GenreSerializer()
    playlist = PlaylistSerializer(many=True)
    class Meta:
        model = Song
        fields = "__all__"

class AlbumViewSetSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Album
        fields = "__all__"