# Generated by Django 3.2 on 2021-04-19 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_api', '0002_alter_file_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file',
            new_name='image',
        ),
    ]
