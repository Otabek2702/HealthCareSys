# Generated by Django 4.0.5 on 2022-06-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthOnline', '0002_patient_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(null=True, upload_to='DoctorImage'),
        ),
    ]