from django.contrib import admin
from django.db import models
from django.http import HttpResponseRedirect

# from .forms import CustomFileInput
from .forms import ItemForm, AdminImageWidget
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    list_display = ['id', 'upload', 'thumbnail']
    list_display_links = ['id', 'upload']
    # readonly_fields = ['file_id', ]
    formfield_overrides = {models.FileField: {'widget': AdminImageWidget}}
    # def formfield_for_dbfield(self, db_field, request, **kwargs):
    #     if db_field.name == 'upload':
    #         kwargs['widget'] = CustomFileInput
    #     return super().formfield_for_dbfield(db_field, request, **kwargs)

    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     print(request, request.__dict__)
    # def response_change(self, request, obj):
    #     print(request.POST)
    #     print(obj)
    #     return super().response_change(request, obj)

    fieldsets = (
        # (None, {
        #     'fields': (
        #         'tg_id', 'first_name', 'last_name', 'username', 'phone', 'tg_user_type', 'balance', 'created',
        #         'updated', 'refer')
        # }),
        ('Загрузить изображение', {
            'fields': ('upload', 'from_storage', 'url'),
        }),

    )

admin.site.register(Item, ItemAdmin)
