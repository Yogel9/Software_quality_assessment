# Generated by Django 4.0.3 on 2023-12-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Halstead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n1', models.FloatField()),
                ('n2', models.FloatField()),
                ('bn1', models.FloatField()),
                ('bn2', models.FloatField()),
                ('k', models.FloatField()),
            ],
        ),
    ]