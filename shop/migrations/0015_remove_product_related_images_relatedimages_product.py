# Generated by Django 4.0.3 on 2022-04-15 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_relatedimages_alter_images_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='related_images',
        ),
        migrations.AddField(
            model_name='relatedimages',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
