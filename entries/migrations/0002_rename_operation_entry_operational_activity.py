# Generated by Django 5.2 on 2025-04-14 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='operation',
            new_name='operational_activity',
        ),
    ]
