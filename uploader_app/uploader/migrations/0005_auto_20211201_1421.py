# Generated by Django 3.2.9 on 2021-12-01 14:21

from django.db import migrations, models
import upload_app.models
import upload_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0004_auto_20211201_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='from_storage',
            field=models.FilePathField(blank=True, default=None, null=True, path=upload_app.models.images_path, verbose_name='From Storage'),
        ),
        migrations.AlterField(
            model_name='item',
            name='upload',
            field=models.FileField(blank=True, default=None, null=True, upload_to='uploads', validators=[upload_app.validators.validate_file_extension]),
        ),
    ]
