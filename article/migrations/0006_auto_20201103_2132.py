# Generated by Django 2.2.4 on 2020-11-03 19:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20201102_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 3, 19, 32, 26, 437701, tzinfo=utc), verbose_name='Article Date'),
        ),
    ]
