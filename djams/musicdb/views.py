from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.
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

#    def put()