# Generated by Django 5.2 on 2025-04-24 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0001_initial'),
        ('pages', '0018_delete_jobapplication'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('applied', 'Applied'), ('reviewing', 'Under Review'), ('shortlisted', 'Shortlisted'), ('rejected', 'Rejected'), ('offered', 'Job Offered'), ('accepted', 'Offer Accepted')], default='applied', max_length=20)),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='pages.job')),
            ],
        ),
    ]
