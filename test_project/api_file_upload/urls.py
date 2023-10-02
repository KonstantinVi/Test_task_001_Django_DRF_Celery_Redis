from django.urls import path
from api_file_upload.views import FileUploadView
from api_file_upload.views import FileListView


urlpatterns = [
    path("upload/", FileUploadView.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-list'),
]
