# Generated by Django 5.0.6 on 2024-06-27 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artobjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artobject',
            name='collection',
            field=models.TextField(blank=True, verbose_name='Коллекция'),
        ),
        migrations.AddField(
            model_name='artobject',
            name='media',
            field=models.TextField(blank=True, verbose_name='СМИ'),
        ),
        migrations.AddField(
            model_name='authorshow',
            name='cost',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена товара'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artobject',
            name='additional_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Дополнительное изображение'),
        ),
        migrations.AlterField(
            model_name='artobject',
            name='city_sale',
            field=models.CharField(max_length=128, verbose_name='Город продажи'),
        ),
        migrations.AlterField(
            model_name='artobject',
            name='cost_category',
            field=models.IntegerField(choices=[(1, 'до 20 000 руб.'), (2, 'от 20 000 до 50 000 руб.'), (3, '50 000 до 100 000 руб.'), (4, 'от 100 000 до 200 000 руб.'), (5, 'от 200 000 до 500 000 руб.')], verbose_name='Категория цены'),
        ),
        migrations.AlterField(
            model_name='artobject',
            name='end_cost',
            field=models.PositiveBigIntegerField(verbose_name='Итоговая цена'),
        ),
        migrations.AlterField(
            model_name='artobject',
            name='fair_cost',
            field=models.PositiveBigIntegerField(blank=True, verbose_name='Желаемая цена'),
        ),
        migrations.AlterField(
            model_name='artobject',
            name='material',
            field=models.CharField(blank=True, max_length=128, verbose_name='Материал работы'),
        ),
        migrations.AlterField(
            model_name='artobject',
            name='size',
            field=models.CharField(max_length=128, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='authorshow',
            name='year',
            field=models.DateField(verbose_name='Дата проведения'),
        ),
        migrations.AlterField(
            model_name='objectauthor',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=1, verbose_name='Возраст'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='objectauthor',
            name='description',
            field=models.TextField(blank=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='objectauthor',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=128, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='objectauthor',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='objectauthor',
            name='personal_style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='objauthor', to='artobjects.style', verbose_name='Персональный стиль'),
        ),
        migrations.AlterField(
            model_name='objectauthor',
            name='professional_education',
            field=models.CharField(blank=True, max_length=128, verbose_name='Художественное образование'),
        ),
        migrations.AlterField(
            model_name='objectauthor',
            name='year_of_birth',
            field=models.DateField(blank=True, verbose_name='Дата рождения'),
        ),
    ]