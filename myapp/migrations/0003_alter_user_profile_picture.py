# Generated by Django 5.0.4 on 2024-04-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='profile_picture/'),
        ),
    ]
