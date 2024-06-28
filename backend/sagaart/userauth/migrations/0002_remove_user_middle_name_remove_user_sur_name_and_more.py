# Generated by Django 5.0.6 on 2024-06-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauth", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="middle_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="sur_name",
        ),
        migrations.AddField(
            model_name="user",
            name="user_name",
            field=models.CharField(
                blank=True, max_length=150, null=True, verbose_name="ФИО"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True,
                default="test Test",
                max_length=150,
                verbose_name="first name",
            ),
            preserve_default=False,
        ),
    ]