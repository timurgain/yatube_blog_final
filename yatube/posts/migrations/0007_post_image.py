# Generated by Django 2.2.16 on 2021-12-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20211201_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/', verbose_name='Картинка'),
        ),
    ]
