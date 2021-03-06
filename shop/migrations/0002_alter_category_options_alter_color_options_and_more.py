# Generated by Django 4.0.3 on 2022-04-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': 'Цвета'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Фотограия', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Размер', 'verbose_name_plural': 'Размеры'},
        ),
        migrations.AlterModelOptions(
            name='variants',
            options={'verbose_name': 'Вариант', 'verbose_name_plural': 'Варианты'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, default='Межкомнатные двери', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
