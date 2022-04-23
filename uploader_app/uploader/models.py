import os

from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from src import settings
from src.settings import VALID_PHOTO_EXTENSIONS, VALID_VIDEO_EXTENSIONS
from upload_app.validators import validate_file_extension, get_extension


def images_path():
    return os.path.join(settings.MEDIA_ROOT, 'uploads')


class Item(models.Model):
    upload = models.FileField(upload_to='uploads', validators=[validate_file_extension, ])

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id} | {self.upload.name}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('image-view', kwargs={'pk': self.pk})

    def thumbnail(self):
        if self.upload:
            # self.file.name
            ext = get_extension(self.upload.name)
            if ext in VALID_PHOTO_EXTENSIONS:
                return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.upload.url))
            elif ext in VALID_VIDEO_EXTENSIONS:
                return mark_safe('<video width="150" height="150" ><source src="{0}"></video>'.format(self.upload.url))
            else:
                return self.upload.name
        else:
            return '(No image)'
