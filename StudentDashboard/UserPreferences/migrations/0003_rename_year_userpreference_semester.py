# Generated by Django 5.0.7 on 2024-08-08 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserPreferences', '0002_userpreference_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpreference',
            old_name='year',
            new_name='semester',
        ),
    ]
