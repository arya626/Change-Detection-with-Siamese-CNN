# Generated by Django 3.0.6 on 2020-05-10 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changedetection', '0002_image_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='pdf',
        ),
        migrations.AddField(
            model_name='image',
            name='video1',
            field=models.FileField(null=True, upload_to='media/video1/'),
        ),
        migrations.AddField(
            model_name='image',
            name='video2',
            field=models.FileField(null=True, upload_to='media/video2/'),
        ),
    ]
