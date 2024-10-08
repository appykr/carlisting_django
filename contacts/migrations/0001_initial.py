# Generated by Django 5.0.6 on 2024-05-28 20:12

import datetime
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
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=150)),
                ('car_id', models.IntegerField()),
                ('car_title', models.CharField(max_length=150)),
                ('user_city', models.CharField(max_length=20)),
                ('user_state', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(default=True)),
                ('message', models.TextField(blank=True, max_length=500)),
                ('user_id', models.IntegerField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
