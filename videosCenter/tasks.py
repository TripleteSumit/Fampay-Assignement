from time import sleep
from celery import shared_task
from .models import Videos, Thumbnails
from .utils import GetLatestVideos
from django.conf import settings


@shared_task
def get_videos_from_youtube():
    # fetch the lates data from youtube api
    data_collection = settings.API_CLASS_OBJ.get_videos()

    if not "error_msg" in data_collection.keys():
        next_page_number = data_collection.get("next_page")

        # iterate over the incoming data for storing purpose
        for media_data in data_collection.get("data"):

            # fetch the data
            data = media_data
            thumbnails = data.pop("thumbnails")

            # storing the coming data
            video = Videos.objects.create(**data)

            for key, thumbnails_data in thumbnails.items():
                thumbnail = Thumbnails.objects.create(
                    video_id=video.id, **thumbnails_data
                )
