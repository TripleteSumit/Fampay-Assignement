import json
from datetime import datetime
import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError
from django.conf import settings


class GetLatestVideos:

    def __init__(self) -> None:
        # queries
        self.query_params = {
            "part": "snippet",
            "order": "date",
            "type": "video",
            "q": "vlogging",
            "key": settings.API_KEYS[0],
            "publishafter": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        self.query_length = len(settings.PREDEFINED_SEARCH_QUERIES)
        self.search_idx = self.api_key_idx = 0

    def get_videos(self):
        try:
            # getting response
            response = requests.get(
                url=f"{settings.URL}/search", params=self.query_params
            )
            if response.status_code == 200:
                response = response.json()
                next_page = response.get("nextPageToken")
                data = []

                if next_page:
                    self.query_params["pageToken"] = next_page
                else:
                    self.search_idx = (self.search_idx + 1) % self.query_length
                    self.query_params["q"] = settings.PREDEFINED_SEARCH_QUERIES[
                        self.search_idx
                    ]
                # fetching required data i.e. title, description, published datetime, thumbnails
                for item in response.get("items"):
                    if item:
                        video_data = {}
                        item_details = item.get("snippet")

                        # loading datas
                        title = item_details.get("title")
                        description = item_details.get("description")
                        thumbnails = item_details.get("thumbnails")
                        publish_time = item_details.get("publishTime")

                        video_data["title"] = title
                        video_data["description"] = description
                        video_data["thumbnails"] = thumbnails
                        video_data["published_time"] = publish_time
                        data.append(video_data)
                # return the required data
                return {"status": "sucess", "next_page": next_page, "data": data}
            elif response.status_code == 403:
                response = response.json()
                error_msg = response.get("error").get("message")
                if "exceed" in error_msg:
                    self.api_key_idx = (self.api_key_idx + 1) % len(settings.API_KEYS)
                    self.query_params["key"] = settings.API_KEYS[self.api_key_idx]
            return {
                "code": response.status_code,
                "status": "failed",
                "error_msg": response.json(),
            }
        except (
            # incase of internal failuers to get response
            RequestException,
            HTTPError,
            ConnectionError,
            json.JSONDecodeError,
        ) as e:
            return {"error": str(e)}
