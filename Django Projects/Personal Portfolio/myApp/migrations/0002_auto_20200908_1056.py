# Generated by Django 3.1.1 on 2020-09-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalblog',
            name='upload',
            field=models.ImageField(default='default.jpg', upload_to='blog_pics/'),
        ),
    ]