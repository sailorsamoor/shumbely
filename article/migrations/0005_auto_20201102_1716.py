# Generated by Django 2.2.4 on 2020-11-02 15:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20190926_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 2, 15, 16, 53, 383829, tzinfo=utc), verbose_name='Article Date'),
        ),
    ]
