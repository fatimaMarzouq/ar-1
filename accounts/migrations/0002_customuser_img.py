# Generated by Django 3.2.3 on 2021-06-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='img',
            field=models.ImageField(default='profilePic/test.jpg', upload_to='profilePic/'),
        ),
    ]
