# Generated by Django 5.0.6 on 2024-05-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_milage_car_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(),
        ),
    ]
