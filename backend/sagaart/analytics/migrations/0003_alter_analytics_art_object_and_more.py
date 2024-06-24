# Generated by Django 5.0.6 on 2024-06-23 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analytics", "0002_initial"),
        (
            "artobjects",
            "0002_remove_author_awards_remove_author_personal_style_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="analytics",
            name="art_object",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="artobjects.artobject",
            ),
        ),
        migrations.AlterField(
            model_name="analytics",
            name="object_author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="artobjects.objectauthor",
            ),
        ),
        migrations.AlterField(
            model_name="authorshow",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="artobjects.objectauthor",
                verbose_name="Автор",
            ),
        ),
    ]