# Generated by Django 4.0.3 on 2022-04-16 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_images_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='type',
        ),
    ]
