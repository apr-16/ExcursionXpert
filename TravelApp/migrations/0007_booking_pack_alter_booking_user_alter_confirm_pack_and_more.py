# Generated by Django 4.2.6 on 2023-10-27 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TravelApp', '0006_booking_alter_packages_date_confirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='pack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TravelApp.packages'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TravelApp.user_reg'),
        ),
        migrations.AlterField(
            model_name='confirm',
            name='pack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TravelApp.packages'),
        ),
        migrations.AlterField(
            model_name='confirm',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TravelApp.user_reg'),
        ),
    ]
