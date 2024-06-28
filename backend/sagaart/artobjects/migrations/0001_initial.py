# Generated by Django 5.0.6 on 2024-06-28 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuthorAward",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название"),
                ),
            ],
            options={
                "verbose_name": "Награда",
                "verbose_name_plural": "Награды",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AuthorShow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название"),
                ),
                (
                    "place",
                    models.CharField(max_length=128, verbose_name="Место"),
                ),
                (
                    "cost",
                    models.PositiveIntegerField(verbose_name="Цена товара"),
                ),
                ("year", models.DateField(verbose_name="Дата проведения")),
            ],
            options={
                "verbose_name": "Выставка",
                "verbose_name_plural": "Выставки",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название"),
                ),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Style",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название"),
                ),
            ],
            options={
                "verbose_name": "Стиль",
                "verbose_name_plural": "Стили",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ObjectAuthor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=128, verbose_name="Имя автора"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[(1, "Male"), (2, "Female")],
                        max_length=128,
                        verbose_name="Пол",
                    ),
                ),
                (
                    "age",
                    models.PositiveIntegerField(
                        blank=True, verbose_name="Возраст"
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(blank=True, verbose_name="Дата рождения"),
                ),
                (
                    "city_of_birth",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        verbose_name="Город рождения",
                    ),
                ),
                (
                    "city_live",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        verbose_name="Город проживания",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Биография"),
                ),
                (
                    "education",
                    models.CharField(
                        blank=True, max_length=128, verbose_name="Образование"
                    ),
                ),
                (
                    "professional_education",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        verbose_name="Художественное образование",
                    ),
                ),
                (
                    "teaching_experience",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        verbose_name="Опыт преподования",
                    ),
                ),
                (
                    "socials",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        verbose_name="Социальные сети",
                    ),
                ),
                (
                    "awards",
                    models.ManyToManyField(
                        blank=True,
                        to="artobjects.authoraward",
                        verbose_name="Награды автора",
                    ),
                ),
                (
                    "show",
                    models.ManyToManyField(
                        blank=True,
                        to="artobjects.authorshow",
                        verbose_name="Выставки автора",
                    ),
                ),
                (
                    "personal_style",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="objauthor",
                        to="artobjects.style",
                        verbose_name="Персональный стиль",
                    ),
                ),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
            },
        ),
        migrations.CreateModel(
            name="ArtObject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="", verbose_name="Изображение"
                    ),
                ),
                (
                    "additional_image",
                    models.ImageField(
                        blank=True,
                        upload_to="",
                        verbose_name="Дополнительное изображение",
                    ),
                ),
                (
                    "size_category",
                    models.IntegerField(
                        choices=[
                            (1, "Любой"),
                            (2, "Small (до 40 см)"),
                            (3, "Medium (40 - 100 см)"),
                            (4, "Large (100 - 160 см)"),
                            (5, "Oversize (более 160 см)"),
                        ],
                        verbose_name="Категория размера",
                    ),
                ),
                (
                    "size",
                    models.CharField(max_length=128, verbose_name="Размер"),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        verbose_name="Страна товара",
                    ),
                ),
                (
                    "city_sale",
                    models.CharField(
                        max_length=128, verbose_name="Город продажи"
                    ),
                ),
                (
                    "year",
                    models.PositiveBigIntegerField(
                        verbose_name="Год создания"
                    ),
                ),
                (
                    "material",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        verbose_name="Материал работы",
                    ),
                ),
                (
                    "tablet_material",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        verbose_name="Материал планшета",
                    ),
                ),
                (
                    "collection",
                    models.TextField(blank=True, verbose_name="Коллекция"),
                ),
                ("media", models.TextField(blank=True, verbose_name="СМИ")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Описание"),
                ),
                (
                    "cost_category",
                    models.IntegerField(
                        choices=[
                            (1, "до 20 000 руб."),
                            (2, "от 20 000 до 50 000 руб."),
                            (3, "50 000 до 100 000 руб."),
                            (4, "от 100 000 до 200 000 руб."),
                            (5, "от 200 000 до 500 000 руб."),
                        ],
                        verbose_name="Категория цены",
                    ),
                ),
                (
                    "end_cost",
                    models.PositiveBigIntegerField(
                        verbose_name="Итоговая цена"
                    ),
                ),
                (
                    "fair_cost",
                    models.PositiveBigIntegerField(
                        blank=True, verbose_name="Желаемая цена"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False, verbose_name="Опубликован"
                    ),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        to="artobjects.category", verbose_name="Категория"
                    ),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        to="artobjects.genre", verbose_name="Жанр"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="atrobj",
                        to="artobjects.objectauthor",
                        verbose_name="Автор",
                    ),
                ),
                (
                    "style",
                    models.ManyToManyField(
                        to="artobjects.style", verbose_name="Стиль"
                    ),
                ),
            ],
            options={
                "verbose_name": "Арт объект",
                "verbose_name_plural": "Арт объекты",
            },
        ),
    ]
