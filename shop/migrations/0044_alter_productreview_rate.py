# Generated by Django 4.0.3 on 2022-05-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0043_productreview_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]