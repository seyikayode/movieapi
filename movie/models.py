from django.db import models

# Create your models here.


class MovieType(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class MediaType(models.Model):
    movie_type = models.ForeignKey(MovieType, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    cast = models.TextField()
    season = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['-movie_type']

    def __str__(self):
        return f'{self.movie_type.category} - {self.movie_name} {self.season}'


class Videos(models.Model):
    movie_type = models.ForeignKey(MovieType, on_delete=models.CASCADE)
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    episode = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    thumbnail = models.ImageField()
    video = models.FileField()

    class Meta:
        verbose_name_plural = "Videos"
        ordering = ['-media_type']

    def __str__(self):
        return f'{self.media_type.movie_type.category} - {self.media_type.movie_name} {self.episode}'