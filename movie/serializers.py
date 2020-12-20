from rest_framework import serializers
from .models import MovieType, MediaType, Videos


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = "__all__"


class MediaTypeSerializer(serializers.ModelSerializer):
    videos = VideosSerializer(many=True, required=False)

    class Meta:
        model = MediaType
        fields = "__all__"


class MovieTypeSerializer(serializers.ModelSerializer):
    media_types = MediaTypeSerializer(many=True, required=False)

    class Meta:
        model = MovieType
        fields = "__all__"