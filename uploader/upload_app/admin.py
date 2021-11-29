from django.contrib import admin
from django.http import HttpResponseRedirect

# from .forms import CustomFileInput
from .forms import CustomFileInput, ItemForm
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    form = ItemForm

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'upload':
            kwargs['widget'] = CustomFileInput
        return super().formfield_for_dbfield(db_field, request, **kwargs)

    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     print(request, request.__dict__)
    # def response_change(self, request, obj):
    #     print(request.POST)
    #     print(obj)
    #     return super().response_change(request, obj)


admin.site.register(Item, ItemAdmin)
