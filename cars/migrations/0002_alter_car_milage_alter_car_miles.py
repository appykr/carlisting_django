# Generated by Django 5.0.6 on 2024-05-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='milage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.IntegerField(),
        ),
    ]