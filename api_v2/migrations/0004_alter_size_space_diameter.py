# Generated by Django 5.1.1 on 2024-10-09 16:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0003_rename_long_range_ft_creatureactionattack_long_range_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='space_diameter',
            field=models.FloatField(blank=True, help_text='Used to measure distance.', null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
