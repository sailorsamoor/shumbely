# Generated by Django 2.2.4 on 2020-11-04 17:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20201103_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 4, 17, 31, 23, 224721, tzinfo=utc), verbose_name='Article Date'),
        ),
    ]