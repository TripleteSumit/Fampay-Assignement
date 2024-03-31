from rest_framework import serializers
from .models import Videos, Thumbnails


class ThumbnailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnails
        fields = ("url", "width", "height")


class VideoSerializer(serializers.ModelSerializer):
    thumbnails = ThumbnailsSerializer(many=True)

    class Meta:
        model = Videos
        fields = ("title", "description", "published_time", "thumbnails")

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        thumbnails = rep.get("thumbnails")
        customize_data = {}
        if thumbnails:
            for thumbnail in thumbnails:
                width = thumbnail.get("width")
                height = thumbnail.get("height")
                url = thumbnail.get("url")
                details = {"url": url, "width": width, "height": height}
                if width == 120 and height == 90:
                    customize_data["default"] = details
                elif width == 320 and height == 180:
                    customize_data["medium"] = details
                else:
                    customize_data["high"] = details
        rep["thumbnails"] = customize_data
        return rep
