# Generated by Django 5.1.2 on 2024-10-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='v2_related_key',
            field=models.TextField(help_text='Key mapping for v2 document.', null=True),
        ),
    ]