from rest_framework import serializers
from .models import File


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'uploaded_at', 'processed')
