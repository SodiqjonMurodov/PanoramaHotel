# Generated by Django 5.0.1 on 2024-03-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='price',
            field=models.IntegerField(),
        ),
    ]
