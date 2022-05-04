# Generated by Django 4.0.3 on 2022-04-15 13:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_description_alter_product_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория', 'verbose_name_plural': '1. Категории'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': '6. Цвета'},
        ),
        migrations.AlterModelOptions(
            name='doortype',
            options={'verbose_name': 'Тип двери', 'verbose_name_plural': '4. Типы двери'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Фотограия', 'verbose_name_plural': '5. Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Дверь', 'verbose_name_plural': '2. Двери'},
        ),
        migrations.AlterModelOptions(
            name='variants',
            options={'verbose_name': 'Вариант', 'verbose_name_plural': '3. Варианты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Количесво'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Детальная информация'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Главное Фото двери'),
        ),
        migrations.AlterField(
            model_name='product',
            name='keywords',
            field=models.CharField(max_length=255, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Наименование Ссылки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='variants',
            name='size',
            field=models.ManyToManyField(to='shop.sizes'),
        ),
    ]
