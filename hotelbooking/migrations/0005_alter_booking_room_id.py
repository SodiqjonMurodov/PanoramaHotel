# Generated by Django 5.0.1 on 2024-03-19 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbooking', '0004_alter_booking_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelbooking.roomtype'),
        ),
    ]
