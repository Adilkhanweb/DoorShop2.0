# Generated by Django 4.0.3 on 2022-04-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0038_remove_variants_images_variants_image_delete_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variants',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
    ]
