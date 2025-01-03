# Generated by Django 4.0.3 on 2023-12-26 18:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HalsteadParam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n1', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Уник. операторов')),
                ('n2', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Уник. операндов')),
                ('hn1', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Общ. операторов')),
                ('hn2', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Общ. операндов')),
                ('k', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Входные/выходные переменные')),
            ],
        ),
    ]