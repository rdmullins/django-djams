from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.http import HttpResponse

# Create your views here.

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumViewSetSerializer
    http_method_names = ["get", "post"]

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongViewSetSerializer
    http_method_names = ["get", "post"]

class AlbumTracksViewSetMultModels(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Album.objects.all(), 'serializer_class': AlbumViewSetSerializer},
        {'queryset': Song.objects.all(), 'serializer_class': SongViewSetSerializer},]
    # queryset = Album.objects.all()
    # serializer_class = AlbumTracksViewSetSerializer
    http_method_names = ["get", "post"]
    # def get_extra_actions():
    #     pass

def AlbumTracksView(request):
    htmlinsert = ""
    albums = list(Album.objects.all())
    for item in albums:
        songlist = ""
        songs = list(Song.objects.filter(album=str(item.id)))
        for song in songs:
            songlist = songlist + "<li>" + str(song.title) + "</li>"
        htmlinsert = htmlinsert + "<li>" + str(item.name) + " (" + str(item.artist.name) + ")" + "<ul>" + songlist + "</ul></li>"
    html = """
    <html>
    <body>
        <h1>Albums and Tracks in the Database:</h1>
        <ul> 
            %s 
        </ul>
    </body>
    </html>""" % htmlinsert

    return HttpResponse(html)

def PlaylistTracksView(request):
    htmlinsert = ""
    playlists = list(Playlist.objects.all())
    for item in playlists:
        songlist = ""
        songs = list(Song.objects.filter(playlist=str(item.id)))
        for song in songs:
            # artist_name = list(Artist.objects.filter(name=str(song.id)))
            songlist = songlist + "<li>" + str(song.title) + "</li>"
        htmlinsert = htmlinsert + "<li>" + str(item.title)  + "<ul>" + songlist + "</ul></li>"
    html = """
    <html>
    <body>
        <h1>Playlists and Tracks in the Database:</h1>
        <ul> 
            %s 
        </ul>
    </body>
    </html>""" % htmlinsert

    return HttpResponse(html)


# Playlist Table 

class PlaylistAPIView(APIView):

# Read Functionality

    def get_object(self, pk):
        try:
            return Playlist.objects.get(pk=pk)
        except Playlist.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = PlaylistSerializer(data)
        else:
            data = Playlist.objects.all()
            serializer = PlaylistSerializer(data, many=True)

        return Response(serializer.data)

# Create Functionality

    def post(self, request, format=None):
        data = request.data
        serializer = PlaylistSerializer(data=data)

        # Check Validity
        serializer.is_valid(raise_exception=True)

        # Save New Playlist
        serializer.save()
        
        # Send Frontend Result
        response = Response()

        response.data = {
            "message": "Playlist Created Successfully",
            "data": serializer.data,
        }

        return response

# Update Functionality

    def put(self, request, pk=None, format=None):
        playlist_update = Playlist.objects.get(pk=pk)
        data = request.data
        serializer = PlaylistSerializer(instance=playlist_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            "message": "Playlist Updated Successfully.",
            "data": serializer.data,
        }

        return response

# Delete Functionality

    def delete(self, request, pk=None, format=None):
        playlist_delete = Playlist.objects.get(pk=pk)
        playlist_delete.delete()
        # data = request.data
        # serializer = PlaylistSerializer(instance=playlist_delete, data=data, partial=True)

        # serializer.is_valid(raise_exception=True)
        # serializer.delete

        response = Response()

        response.data = {
            "message": "Playlist Deleted.",
            # "data": serializer.data,
        }

        return response

# Album Table

class AlbumAPIView(APIView):

# Read Functionality

    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = AlbumSerializer(data)
        else:
            data = Album.objects.all()
            serializer = AlbumSerializer(data, many=True)

        return Response(serializer.data)

# Create Functionality

    def post(self, request, format=None):
        data = request.data
        serializer = AlbumSerializer(data=data)

        # Check Validity
        serializer.is_valid(raise_exception=True)

        # Save New Album
        serializer.save()
        
        # Send Frontend Result
        response = Response()

        response.data = {
            "message": "Album Created Successfully",
            "data": serializer.data,
        }

        return response

# Update Functionality

    def put(self, request, pk=None, format=None):
        album_update = Album.objects.get(pk=pk)
        data = request.data
        serializer = AlbumSerializer(instance=album_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            "message": "Album Updated Successfully.",
            "data": serializer.data,
        }

        return response

# Delete Functionality

    def delete(self, request, pk=None, format=None):
        album_delete = Album.objects.get(pk=pk)
        album_delete.delete()
        # data = request.data
        # serializer = PlaylistSerializer(instance=playlist_delete, data=data, partial=True)

        # serializer.is_valid(raise_exception=True)
        # serializer.delete

        response = Response()

        response.data = {
            "message": "Album Deleted.",
            # "data": serializer.data,
        }

        return response

# Artist Table

class ArtistAPIView(APIView):

# Read Functionality

    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = ArtistSerializer(data)
        else:
            data = Artist.objects.all()
            serializer = ArtistSerializer(data, many=True)

        return Response(serializer.data)

# Create Functionality

    def post(self, request, format=None):
        data = request.data
        serializer = ArtistSerializer(data=data)

        # Check Validity
        serializer.is_valid(raise_exception=True)

        # Save New Artist
        serializer.save()
        
        # Send Frontend Result
        response = Response()

        response.data = {
            "message": "Artist Created Successfully",
            "data": serializer.data,
        }

        return response

# Update Functionality

    def put(self, request, pk=None, format=None):
        artist_update = Artist.objects.get(pk=pk)
        data = request.data
        serializer = ArtistSerializer(instance=artist_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            "message": "Artist Updated Successfully.",
            "data": serializer.data,
        }

        return response

# Delete Functionality

    def delete(self, request, pk=None, format=None):
        artist_delete = Artist.objects.get(pk=pk)
        artist_delete.delete()
        # data = request.data
        # serializer = PlaylistSerializer(instance=playlist_delete, data=data, partial=True)

        # serializer.is_valid(raise_exception=True)
        # serializer.delete

        response = Response()

        response.data = {
            "message": "Artist Deleted.",
            # "data": serializer.data,
        }

        return response

# Genre Table

class GenreAPIView(APIView):

# Read Functionality

    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = GenreSerializer(data)
        else:
            data = Genre.objects.all()
            serializer = GenreSerializer(data, many=True)

        return Response(serializer.data)

# Create Functionality

    def post(self, request, format=None):
        data = request.data
        serializer = GenreSerializer(data=data)

        # Check Validity
        serializer.is_valid(raise_exception=True)

        # Save New Genre
        serializer.save()
        
        # Send Frontend Result
        response = Response()

        response.data = {
            "message": "Genre Created Successfully",
            "data": serializer.data,
        }

        return response

# Update Functionality

    def put(self, request, pk=None, format=None):
        genre_update = Genre.objects.get(pk=pk)
        data = request.data
        serializer = GenreSerializer(instance=genre_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            "message": "Genre Updated Successfully.",
            "data": serializer.data,
        }

        return response

# Delete Functionality

    def delete(self, request, pk=None, format=None):
        genre_delete = Genre.objects.get(pk=pk)
        genre_delete.delete()
        # data = request.data
        # serializer = PlaylistSerializer(instance=playlist_delete, data=data, partial=True)

        # serializer.is_valid(raise_exception=True)
        # serializer.delete

        response = Response()

        response.data = {
            "message": "Genre Deleted.",
            # "data": serializer.data,
        }

        return response

# Song Table

class SongAPIView(APIView):

# Read Functionality

    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SongSerializer(data)
        else:
            data = Song.objects.all()
            serializer = SongSerializer(data, many=True)

        return Response(serializer.data)

# Create Functionality

    def post(self, request, format=None):
        data = request.data
        serializer = SongSerializer(data=data)

        # Check Validity
        serializer.is_valid(raise_exception=True)

        # Save New Song
        serializer.save()
        
        # Send Frontend Result
        response = Response()

        response.data = {
            "message": "Song Created Successfully",
            "data": serializer.data,
        }

        return response

# Update Functionality

    def put(self, request, pk=None, format=None):
        song_update = Song.objects.get(pk=pk)
        data = request.data
        serializer = SongSerializer(instance=song_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            "message": "Song Updated Successfully.",
            "data": serializer.data,
        }

        return response

# Delete Functionality

    def delete(self, request, pk=None, format=None):
        song_delete = Song.objects.get(pk=pk)
        song_delete.delete()
        # data = request.data
        # serializer = PlaylistSerializer(instance=playlist_delete, data=data, partial=True)

        # serializer.is_valid(raise_exception=True)
        # serializer.delete

        response = Response()

        response.data = {
            "message": "Song Deleted.",
            # "data": serializer.data,
        }

        return response