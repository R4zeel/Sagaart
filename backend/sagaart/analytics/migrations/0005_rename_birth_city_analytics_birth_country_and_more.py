# Generated by Django 5.0.6 on 2024-06-25 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "analytics",
            "0004_remove_authorshow_author_remove_analytics_art_object_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="analytics",
            old_name="birth_city",
            new_name="birth_country",
        ),
        migrations.AddField(
            model_name="analytics",
            name="analytics_owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Заказчик аналитки",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="analytics",
            name="calculated_price",
            field=models.IntegerField(null=True),
        ),
    ]