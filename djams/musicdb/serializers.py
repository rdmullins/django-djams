from rest_framework import serializers
from .models import *
from .fields import *

class PlaylistSerializer(serializers.ModelSerializer):
    name = ArtistListingField(many=True, read_only=True)
    playlist_list = PlaylistListingField(many=True, read_only=True, label="Songs")
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

class ArtistSerializerForSongView(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name",)

class AlbumSerializerForSongView(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("name",)

class GenreSerializerForSongView(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("genre",)

class PlaylistSerializerForSongView(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ("title",)

class SongViewSetSerializer(serializers.ModelSerializer):
    artist = ArtistSerializerForSongView(many=True)
    album = AlbumSerializerForSongView(many=True)
    genre = GenreSerializerForSongView()
    playlist = PlaylistSerializerForSongView(many=True)
    class Meta:
        model = Song
        fields = "__all__"

class AlbumViewSetSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    # song = SongViewSetSerializer(many=True)
    class Meta:
        model = Album
        # fields = ["__all__", Song.title,]
        fields = "__all__"

class AlbumTracksViewSetSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    album = AlbumSerializer()
    #song = SongViewSetSerializer(many=True)
    class Meta:
        model = Song
        fields = ("title", "album", "artist")