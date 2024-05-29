# Generated by Django 5.0.4 on 2024-04-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]