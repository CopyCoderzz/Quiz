# Generated by Django 3.2.8 on 2021-11-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0016_rename_img_fil_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='MEDIA')),
            ],
        ),
        migrations.DeleteModel(
            name='fil',
        ),
    ]
