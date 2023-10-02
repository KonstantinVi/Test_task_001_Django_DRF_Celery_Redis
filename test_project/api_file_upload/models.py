from django.db import models


class File(models.Model):
    """
    Модель File.

    Атрибуты:
        + **file** (models.FileField): *Поле для загрузки файла*.
        + **uploaded_at** (models.DateTimeField): *Дата и время загрузки файла*.
        + **processed** (models.BooleanField): *Указывает, был ли файл обработан или нет*.
    """
    file = models.FileField(upload_to='uploaded_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
