# Generated by Django 3.2.9 on 2021-11-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='upload',
            field=models.FileField(upload_to='uploads'),
        ),
    ]