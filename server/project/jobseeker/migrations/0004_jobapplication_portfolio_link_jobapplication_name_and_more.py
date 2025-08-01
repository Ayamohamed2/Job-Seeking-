# Generated by Django 5.2 on 2025-04-26 00:05

import jobseeker.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0003_userprofile_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='Portfolio_link',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=jobseeker.models.user_photo_path),
        ),
    ]
