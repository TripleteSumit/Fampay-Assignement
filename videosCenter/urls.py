from django.urls import path

from .views import VideoView

urlpatterns = [
    path("videos/", view=VideoView.as_view(), name="dummy"),
]
