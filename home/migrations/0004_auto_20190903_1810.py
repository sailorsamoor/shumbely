# Generated by Django 2.2.4 on 2019-09-03 16:10

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_teaser'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='bodyleft_en',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Left section'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='bodyleft_ru',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Left section'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='bodyright_en',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Right section'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='bodyright_ru',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Right section'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='url1',
            field=models.URLField(blank=True, null=True, verbose_name='Get Started'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='url2',
            field=models.URLField(blank=True, null=True, verbose_name='Check Them Out'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Moto'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_ru',
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name='Moto'),
        ),
    ]
