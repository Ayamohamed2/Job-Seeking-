# Generated by Django 5.1.6 on 2025-04-18 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_profile_city_profile_country_profile_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('job_skills', models.TextField(help_text='Comma-separated list of skills')),
                ('salaryoffer', models.CharField(blank=True, max_length=100, null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('edu_qualifications', models.TextField()),
                ('Work_experince', models.TextField()),
                ('Deadline_of_application', models.DateTimeField(blank=True, null=True)),
                ('Emp_type', models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('paid_internship', 'Paid Internship'), ('unpaid_internship', 'Unpaid Internship'), ('freelance', 'Freelance')], default='full_time', max_length=20)),
                ('period', models.CharField(blank=True, help_text='e.g. 6 months, 1 year', max_length=100, null=True)),
            ],
        ),
    ]
