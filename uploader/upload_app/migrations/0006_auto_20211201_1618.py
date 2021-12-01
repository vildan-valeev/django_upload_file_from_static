# Generated by Django 3.2.9 on 2021-12-01 16:18

from django.db import migrations, models
import upload_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0005_auto_20211201_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='from_storage',
        ),
        migrations.AlterField(
            model_name='item',
            name='upload',
            field=models.FileField(default=1, upload_to='uploads', validators=[upload_app.validators.validate_file_extension]),
            preserve_default=False,
        ),
    ]
