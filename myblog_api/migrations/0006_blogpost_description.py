# Generated by Django 3.0.6 on 2020-06-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog_api', '0005_blogpost_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]