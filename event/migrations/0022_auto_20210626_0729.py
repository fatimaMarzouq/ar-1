# Generated by Django 3.2.3 on 2021-06-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0021_auto_20210624_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='Latitude',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='Longitude',
            field=models.CharField(default=121221, max_length=200),
            preserve_default=False,
        ),
    ]
