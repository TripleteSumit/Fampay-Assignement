import json
import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError
from django.conf import settings


class GetLatestVideos:

    # it fetches the current time
    current_time = settings.CURRENT_TIME.strftime("%Y-%m-%dT%H:%M:%SZ")

    # queries
    query_params = {
        "part": "snippet",
        "order": "date",
        "publishafter": current_time,
        "type": "video",
        "q": "gaming",
        "key": settings.API_KEY,
    }

    def get_videos(self):
        try:
            # getting response
            response = requests.get(
                url=f"{settings.URL}/search", params=self.query_params
            )
            # return the response
            return {"code": response.status_code, "data": response.json()}
        except (
            # incase of internal failuers to get response
            RequestException,
            HTTPError,
            ConnectionError,
            json.JSONDecodeError,
        ) as e:
            return {"error": str(e)}
