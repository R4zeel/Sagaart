# Generated by Django 5.0.6 on 2024-06-22 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorAward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Награда',
                'verbose_name_plural': 'Награды',
            },
        ),
        migrations.CreateModel(
            name='AuthorShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('year', models.PositiveIntegerField(verbose_name='Дата проведения')),
                ('place', models.CharField(max_length=128, verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Выставка',
                'verbose_name_plural': 'Выставки',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Стиль',
                'verbose_name_plural': 'Стили',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=128, verbose_name='Пол')),
                ('age', models.PositiveIntegerField(null=True, verbose_name='Возраст')),
                ('year_of_birth', models.PositiveIntegerField(blank=True, verbose_name='Год рождения')),
                ('city_of_birth', models.CharField(blank=True, max_length=128, verbose_name='Город рождения')),
                ('city_live', models.CharField(blank=True, max_length=128, verbose_name='Город проживания')),
                ('education', models.CharField(blank=True, max_length=128, verbose_name='Образование')),
                ('professional_education', models.CharField(blank=True, max_length=128, verbose_name='Профессиональное образование')),
                ('teaching_experience', models.CharField(blank=True, max_length=128, verbose_name='Опыт преподования')),
                ('socials', models.CharField(blank=True, max_length=128, verbose_name='Социальные сети')),
                ('awards', models.ManyToManyField(blank=True, to='artobjects.authoraward', verbose_name='Награды автора')),
                ('show', models.ManyToManyField(blank=True, to='artobjects.authorshow', verbose_name='Выставки автора')),
                ('personal_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='objauthor', to='artobjects.style', verbose_name='Стиль')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('additional_image', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
                ('size_category', models.IntegerField(choices=[(1, 'Any'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Oversize')], verbose_name='Категория размера')),
                ('size', models.CharField(blank=True, max_length=128, verbose_name='Размер')),
                ('country', models.CharField(blank=True, max_length=128, verbose_name='Город')),
                ('city_sale', models.CharField(blank=True, max_length=128, verbose_name='Город продажи')),
                ('year', models.PositiveBigIntegerField(verbose_name='Год создания')),
                ('material', models.CharField(blank=True, max_length=128, verbose_name='Материал')),
                ('tablet_material', models.CharField(blank=True, max_length=128, verbose_name='Материал планшета')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='Описание')),
                ('cost_category', models.IntegerField(choices=[(1, 'PRICE_SMALL'), (2, 'PRICE_MEDIUM'), (3, 'PRICE_LARGE')], verbose_name='Ценовая категория')),
                ('end_cost', models.IntegerField(blank=True, verbose_name='Финальная цена')),
                ('fair_cost', models.IntegerField(blank=True, verbose_name='Оценка')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликован')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atrobj', to='artobjects.author', verbose_name='Автор')),
                ('category', models.ManyToManyField(to='artobjects.category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(to='artobjects.genre', verbose_name='Жанр')),
                ('style', models.ManyToManyField(to='artobjects.style', verbose_name='Стиль')),
            ],
            options={
                'verbose_name': 'Арт объект',
                'verbose_name_plural': 'Арт объекты',
            },
        ),
    ]
