# Generated by Django 4.0.3 on 2022-05-08 17:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0047_alter_banner_options_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='service',
            name='services',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Услуга'),
        ),
    ]
