# Generated by Django 2.2.4 on 2019-09-12 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puput', '0003_entrypage_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrypage',
            name='video_url',
        ),
    ]
