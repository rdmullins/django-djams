from django.urls import path
from .views import *

urlpatterns = [
    path("playlist/", PlaylistAPIView.as_view()),
    path("playlist/<str:pk>/", PlaylistAPIView.as_view()),
]