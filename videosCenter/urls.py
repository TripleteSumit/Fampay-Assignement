from django.urls import path
from django.views.generic import TemplateView

from .views import VideoView

urlpatterns = [
    path("videos/", view=VideoView.as_view(), name="dummy"),
    path("", view=TemplateView.as_view(template_name="Home.html"), name="home-page"),
]
