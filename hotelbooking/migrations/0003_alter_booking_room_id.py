# Generated by Django 5.0.1 on 2024-03-18 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0002_alter_roomtype_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelbooking.roomtype'),
        ),
    ]
