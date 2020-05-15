# Generated by Django 3.0.5 on 2020-05-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200514_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_toc',
            field=models.BooleanField(default=False, verbose_name='TOC'),
        ),
        migrations.AddField(
            model_name='post',
            name='toc_depth',
            field=models.PositiveSmallIntegerField(default=6, verbose_name='TOC depth'),
        ),
    ]
