# Generated by Django 3.0.4 on 2020-03-21 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='phone x', max_length=16),
        ),
        migrations.AlterField(
            model_name='request',
            name='address',
            field=models.CharField(default='address x', max_length=32),
        ),
        migrations.AlterField(
            model_name='request',
            name='city',
            field=models.CharField(default='city x', max_length=32),
        ),
        migrations.AlterField(
            model_name='request',
            name='zip_code',
            field=models.CharField(default='zip code x', max_length=10),
        ),
    ]
