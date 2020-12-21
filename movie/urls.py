from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("api/movies/", views.MovieTypeList.as_view()),
    path("api/add_movie/", views.MovieTypeCreate.as_view()),
    path("api/movies/<int:pk>/", views.MovieTypeDetail.as_view()),
    path("api/movies/<int:pk>/medias/", views.MediaTypeList.as_view()),
    path("api/movies/<int:pk>/add_media/", views.MediaTypeCreate.as_view()),
    path("api/movies/<int:pk>/medias/<int:media_pk>/", views.MediaTypeDetail.as_view()),
    path("api/movies/<int:pk>/medias/<int:media_pk>/videos/", views.VideoList.as_view()),
    path("api/movies/<int:pk>/medias/<int:media_pk>/add_video/", views.VideoCreate.as_view()),
    path("api/movies/<int:pk>/medias/<int:media_pk>/videos/<int:video_pk>/", views.VideoDetail.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)