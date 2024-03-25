from django.db import models


class Thumbnails(models.Model):
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()

class Videos(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    publishing_datetime = models.DateTimeField()
    thumbnails = models.OneToOneField(Thumbnails, on_delete=models.CASCADE, related_name='videos_img')