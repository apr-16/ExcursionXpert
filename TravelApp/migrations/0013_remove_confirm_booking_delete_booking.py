# Generated by Django 4.2.6 on 2023-10-28 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TravelApp', '0012_alter_confirm_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirm',
            name='booking',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
