from django.db import models


class Videos(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    published_time = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.title}-{self.published_time}"


class Thumbnails(models.Model):
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    video = models.ForeignKey(
        Videos, on_delete=models.CASCADE, related_name="thumnails"
    )

    def __str__(self) -> str:
        return f"{self.video}-{self.url}"
