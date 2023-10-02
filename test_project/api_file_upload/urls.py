from django.urls import path
from api_file_upload.views import FileUploadView


urlpatterns = [
    path("upload/", FileUploadView.as_view(), name='file-upload'),
]
