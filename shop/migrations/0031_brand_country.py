# Generated by Django 4.0.3 on 2022-04-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_alter_product_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]