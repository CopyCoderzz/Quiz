# Generated by Django 3.2.8 on 2021-11-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0022_auto_20211119_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizfile',
            name='exm_name',
            field=models.DateField(null=True),
        ),
    ]
