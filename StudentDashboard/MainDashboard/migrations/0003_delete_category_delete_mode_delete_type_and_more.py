# Generated by Django 5.0.7 on 2024-08-08 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainDashboard', '0002_upcomingcompanydetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Mode',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]
