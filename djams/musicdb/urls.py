from django.urls import path
from .views import *

urlpatterns = [
    path("playlist/", PlaylistAPIView.as_view()),
    path("playlist/<str:pk>/", PlaylistAPIView.as_view()),
    path("album/", AlbumAPIView.as_view()),
    path("album/<str:pk>/", AlbumAPIView.as_view()),
    path("artist/", ArtistAPIView.as_view()),
    path("artist/<str:pk>/", ArtistAPIView.as_view()),
]