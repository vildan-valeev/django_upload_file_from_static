import os

from django import forms
from django.conf import settings
from django.contrib.admin.widgets import AdminFileWidget
from django.db.models.fields.files import FieldFile
from django.forms import widgets
from django.utils.html import format_html

from src.settings import VALID_PHOTO_EXTENSIONS, VALID_VIDEO_EXTENSIONS
from upload_app.models import Item
from upload_app.validators import get_extension


def images_path():
    return os.path.join(settings.MEDIA_ROOT, 'uploads')


# print(images_path())
class CheckFieldsMixin:
    def check_fullness(self, clean_dict: dict) -> bool:
        """
        check dict. In dict will be only one NoneType, non-False
        """
        # есть ли хоть один None, все ли значения в списке None ()
        if len({k: v for k, v in clean_dict.items() if v}) == 1:
            return True
        return False

class ItemForm(forms.ModelForm, CheckFieldsMixin):
    from_storage = forms.FilePathField(
        path='/home/vildan/PycharmProjects/django_upload_file_from_static/uploader/media/uploads', required=None)
    url = forms.URLField(required=None, help_text='https://example.com/image.png')

    class Meta:
        model = Item
        fields = ['upload', 'from_storage', 'url']

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        if not self.check_fullness(cleaned_data):
            raise forms.ValidationError('Необходимо что-то одно - загрузите файл, '
                                        'выберите существующий, или вставьте ссылку на изображение')
        return cleaned_data


# class CustomFileInput(widgets.ClearableFileInput):
#     template_name = 'admin/widgets/upload_app/item/custom_clearable_file_input.html'


class AdminImageWidget(AdminFileWidget):

    def render(self, name, value: FieldFile, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and getattr(value, 'url', None):
            ext = get_extension(value.name)
            if ext in VALID_PHOTO_EXTENSIONS:
                html = format_html(
                    '<a href="{0}" target="_blank"><img src="{0}" alt="{1}" width="150" height="150" '
                    'style="object-fit: contain;"/></a>',
                    value.url, str(value)) + html
                return html
            if ext in VALID_VIDEO_EXTENSIONS:
                html = format_html(
                    '<a href="{0}" target="_blank"><video width="150" height="150" ><source src="{0}"></video></a>',
                    value.url, str(value)) + html
                return html
        return html
