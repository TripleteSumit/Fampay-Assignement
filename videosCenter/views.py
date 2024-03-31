from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Videos, Thumbnails
from .pagination import VideosPagination
from .serializer import VideoSerializer


class VideoView(APIView, VideosPagination):

    def get(self, request):

        query_params = request.query_params
        if not self.get_page_size(request) in range(
            self.page_size, self.max_page_size + 1
        ):
            return Response(
                data={
                    "status": "failed",
                    "msg": f"Range of page size is in between {self.page_size}-{self.max_page_size}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        videos = (
            Videos.objects.prefetch_related("thumbnails")
            .all()
            .order_by("-published_time")
        )
        data = self.paginate_queryset(videos, request)
        serializer = VideoSerializer(data, many=True)
        return self.get_paginated_response(
            {"status": "success", "data": serializer.data}
        )
