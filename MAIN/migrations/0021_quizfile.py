# Generated by Django 3.2.8 on 2021-11-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0020_delete_quizfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='file')),
            ],
        ),
    ]
