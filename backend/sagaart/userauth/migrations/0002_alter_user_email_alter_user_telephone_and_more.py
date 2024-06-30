# Generated by Django 5.0.6 on 2024-06-30 12:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=250, unique=True, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=150, null=True, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='ФИО'),
        ),
        migrations.DeleteModel(
            name='UserSubscribe',
        ),
    ]
