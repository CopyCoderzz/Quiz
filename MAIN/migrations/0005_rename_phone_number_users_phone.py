# Generated by Django 3.2.8 on 2021-10-25 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0004_quesmodel_exp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
