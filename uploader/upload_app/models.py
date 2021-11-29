from django.db import models
from django.urls import reverse


class Item(models.Model):
    upload = models.FileField(upload_to='uploads')

    def __str__(self):
        return f'{self.id} | {self.upload.name}'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('image-view', kwargs={'pk': self.pk})

