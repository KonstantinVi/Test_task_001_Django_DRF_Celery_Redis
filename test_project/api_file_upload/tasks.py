from celery import shared_task
from .models import File


@shared_task
def process_file(file_id):
    file_instance = File.objects.get(id=file_id)
    # Доп код для обработки файла
    file_instance.processed = True
    file_instance.save()


@shared_task
def add_test(x, y):
    """Задача для тестирования связки Celery + Redis."""
    return x + y
