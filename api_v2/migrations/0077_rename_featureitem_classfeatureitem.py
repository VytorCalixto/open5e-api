# Generated by Django 3.2.20 on 2024-05-25 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0076_auto_20240524_1727'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeatureItem',
            new_name='ClassFeatureItem',
        ),
    ]