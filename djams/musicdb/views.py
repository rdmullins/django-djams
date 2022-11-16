from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.

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

