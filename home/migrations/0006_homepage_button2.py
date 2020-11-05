# Generated by Django 2.2.4 on 2019-09-07 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0005_homepage_button1'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='button2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
