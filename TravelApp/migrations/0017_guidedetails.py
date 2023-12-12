# Generated by Django 4.2.6 on 2023-10-29 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TravelApp', '0016_remove_payment_cardtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='guidedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=50, null=True)),
                ('dis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TravelApp.district')),
            ],
        ),
    ]