# Generated by Django 2.2.4 on 2019-09-12 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_button2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='url1',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='url2',
        ),
    ]
