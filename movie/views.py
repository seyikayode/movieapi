from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import MovieType, MediaType, Videos
from .serializers import VideosSerializer, MediaTypeSerializer, MovieTypeSerializer
# Create your views here.


class MovieTypeList(APIView):
    def get(self, request):
        types = MovieType.objects.all()
        data = MovieTypeSerializer(types, many=True).data
        return Response(data)


class MediaTypeList(APIView):
    def get(self, request, pk):
        types = get_object_or_404(MovieType, pk=pk)
        media = MediaType.objects.filter(movie_type_id=types)
        data = MediaTypeSerializer(media, many=True).data
        return Response(data)  


class VideoList(APIView):
    def get(self, request, pk, pk2):
        types = get_object_or_404(MovieType, pk=pk)
        media = get_object_or_404(MediaType, movie_type_id=types, pk=pk2)
        video = Videos.objects.filter(media_type_id=media)
        data = VideosSerializer(video, many=True).data
        return Response(data)
        