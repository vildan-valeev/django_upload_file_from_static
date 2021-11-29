import os

from django import forms
from django.conf import settings
from django.forms import widgets

from upload_app.models import Item


def images_path():
    return os.path.join(settings.MEDIA_ROOT, 'uploads')


print(images_path())


class ItemForm(forms.ModelForm):
    # storage = forms.FilePathField(path=images_path)
    storage = forms.FilePathField(
        path='/home/vildan/PycharmProjects/django_upload_file_from_static/uploader/media/uploads',)

    class Meta:
        model = Item
        fields = ['upload', 'storage']

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        return cleaned_data


class CustomFileInput(widgets.ClearableFileInput):
    template_name = 'admin/widgets/upload_app/item/custom_clearable_file_input.html'
