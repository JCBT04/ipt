# Generated by Django 5.1.6 on 2025-02-21 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_pick_location_booking_pickup_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='booking',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='booking.booking'),
        ),
    ]
