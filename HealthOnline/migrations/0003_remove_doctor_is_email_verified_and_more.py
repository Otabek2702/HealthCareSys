# Generated by Django 4.1 on 2022-08-10 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HealthOnline', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='is_email_verified',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='is_email_verified',
        ),
    ]
