# Generated by Django 4.2.6 on 2023-10-28 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TravelApp', '0011_alter_confirm_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirm',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='TravelApp.booking'),
        ),
    ]
