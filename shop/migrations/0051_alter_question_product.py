# Generated by Django 4.0.3 on 2022-05-08 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0050_question_answered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
