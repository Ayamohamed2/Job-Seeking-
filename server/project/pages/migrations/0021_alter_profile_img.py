# Generated by Django 5.2 on 2025-05-02 12:23

import pages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_alter_profile_vision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='Profiles/68/photos/default.png', null=True, upload_to=pages.models.user_photo_path),
        ),
    ]
