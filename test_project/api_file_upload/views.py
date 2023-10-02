from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import File
from .serializers import UploadedFileSerializer
from .tasks import process_file


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = UploadedFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            # Запуск асинхронной задачи Celery.
            process_file.delay(file_serializer.instance.id)
            return Response(file_serializer.data, status=201)
        else:
            return Response(file_serializer.errors, status=400)
