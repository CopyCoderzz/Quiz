# Generated by Django 3.2.8 on 2021-11-18 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0018_rename_file_upload_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='upload_file',
            new_name='Quizfile',
        ),
    ]
