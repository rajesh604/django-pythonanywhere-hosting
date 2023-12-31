# Generated by Django 4.2.2 on 2023-06-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='gmail',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='booking',
            name='comment',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='booking',
            name='first_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='last_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
