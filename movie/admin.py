from django.contrib import admin
from .models import MovieType, MediaType, Videos
# Register your models here.


admin.site.register(MovieType)
admin.site.register(MediaType)
admin.site.register(Videos)