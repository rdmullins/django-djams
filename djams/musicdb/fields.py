from rest_framework import serializers
from .models import *

class ArtistListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name

class PlaylistListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.title