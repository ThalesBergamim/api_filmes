# Generated by Django 5.1.5 on 2025-02-01 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release_data',
            new_name='release_date',
        ),
    ]
