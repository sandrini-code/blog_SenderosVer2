# Generated by Django 4.0 on 2022-12-03 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='actuvado',
            new_name='activado',
        ),
    ]
