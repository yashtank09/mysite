# Generated by Django 4.0.7 on 2023-03-05 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='milage',
            new_name='mileage',
        ),
    ]