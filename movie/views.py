from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from django.shortcuts import get_object_or_404
from .models import MovieType, MediaType, Videos
from .serializers import VideosSerializer, MediaTypeSerializer, MovieTypeSerializer
# Create your views here.


class MovieTypeList(APIView):
    def get(self, request):
        types = MovieType.objects.all()
        data = MovieTypeSerializer(types, many=True).data
        return Response(data)


class MovieTypeCreate(APIView):
    def post(self, request, *args, **kwargs):
        movie_serializer = MovieTypeSerializer(data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieTypeDetail(APIView):
    def get(self, request, pk):
        types = get_object_or_404(MovieType, pk=pk)
        data = MovieTypeSerializer(types).data
        return Response(data)


class MediaTypeList(APIView):
    def get(self, request, pk):
        types = get_object_or_404(MovieType, pk=pk)
        media = MediaType.objects.filter(movie_type_id=types)
        data = MediaTypeSerializer(media, many=True).data
        return Response(data)


class MediaTypeCreate(APIView):
    def post(self, request, pk):
        # types = get_object_or_404(MovieType, pk=pk)
        movie_name = request.data.get('movie_name')
        genre = request.data.get('genre')
        cast = request.data.get('cast')
        season = request.data.get('season')
        data = {'movie_type': pk, 'movie_name': movie_name, 'genre': genre, 'cast': cast,
               'season': season}
        serializer = MediaTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MediaTypeDetail(APIView):
    def get(self, request, pk, media_pk):
        types = get_object_or_404(MovieType, pk=pk)
        media = MediaType.objects.filter(movie_type_id=types, pk=media_pk)
        data = MediaTypeSerializer(media, many=True).data
        return Response(data)


class VideoList(APIView):
    def get(self, request, pk, media_pk):
        types = get_object_or_404(MovieType, pk=pk)
        media = get_object_or_404(MediaType, movie_type_id=types, pk=media_pk)
        video = Videos.objects.filter(media_type_id=media)
        data = VideosSerializer(video, many=True).data
        return Response(data)


class VideoCreate(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, pk, media_pk):
        # types = get_object_or_404(MovieType, pk=pk)
        # media = get_object_or_404(MediaType, movie_type_id=types, pk=pk2)
        episode = request.data.get('episode')
        description = request.data.get('description')
        thumbnail = request.data.get('thumbnail')
        video = request.data.get('video')
        data = {'movie_type': pk, 'media_type': media_pk, 'episode': episode, 'description': description,
               'thumbnail': thumbnail, 'video': video}
        video_serializer = VideosSerializer(data=data)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoDetail(APIView):
    def get(self, request, pk, media_pk, video_pk):
        types = get_object_or_404(MovieType, pk=pk)
        media = get_object_or_404(MediaType, movie_type_id=types, pk=media_pk)
        video = Videos.objects.filter(media_type_id=media, pk=video_pk)
        data = VideosSerializer(video, many=True).data
        return Response(data)

# class MediaTypeDetail(APIView):
#     def get(self, request, pk, media_pk):
#         types = get_object_or_404(MovieType, pk=pk)
#         media = MediaType.objects.filter(movie_type_id=types, pk=media_pk)
#         data = MediaTypeSerializer(media, many=True).data
#         return Response(data)