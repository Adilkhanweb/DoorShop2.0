# Generated by Django 4.0.3 on 2022-04-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_remove_product_related_images_relatedimages_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='variants',
            name='sale_percent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='variants',
            name='sale_price',
            field=models.FloatField(default=0),
        ),
    ]