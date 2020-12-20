from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("api/movie/", views.MovieTypeList.as_view()),
    path("api/movie/<int:pk>/", views.MediaTypeList.as_view()),
    path("api/movie/<int:pk>/video/<int:pk2>/", views.VideoList.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)