# Generated by Django 4.2.6 on 2023-10-29 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TravelApp', '0015_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='cardtype',
        ),
    ]
