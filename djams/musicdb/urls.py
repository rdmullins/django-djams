from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"albums", AlbumViewSet)
router.register(r"songs", SongViewSet)
#router.register(r"albumtracks", AlbumTracksViewSet.as_view(), basename="albumtracks")

urlpatterns = [
    path("playlist/", PlaylistAPIView.as_view()),
    path("playlist/<str:pk>/", PlaylistAPIView.as_view()),
    path("album/", AlbumAPIView.as_view()),
    path("album/<str:pk>/", AlbumAPIView.as_view()),
    path("artist/", ArtistAPIView.as_view()),
    path("artist/<str:pk>/", ArtistAPIView.as_view()),
    path("genre/", GenreAPIView.as_view()),
    path("genre/<str:pk>/", GenreAPIView.as_view()),
    path("song/", SongAPIView.as_view()),
    path("song/<str:pk>/", SongAPIView.as_view()),
    path("albumtracks/", views.AlbumTracksView),
    path("playlisttracks/", views.PlaylistTracksView),
    path("", include(router.urls))
]