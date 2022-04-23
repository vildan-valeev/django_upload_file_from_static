import os

from django.core.exceptions import ValidationError

from src.settings import VALID_PHOTO_EXTENSIONS, VALID_VIDEO_EXTENSIONS


def get_extension(name: str) -> str:
    return os.path.splitext(name)[1]


def validate_file_extension(value):
    ext = get_extension(value.name)  # [0] returns path+filename
    valid_extensions = VALID_VIDEO_EXTENSIONS + VALID_PHOTO_EXTENSIONS
    if not ext.lower() in valid_extensions:
        raise ValidationError('Неверный формат изображения. Требуются изображения или видео')


