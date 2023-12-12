# Generated by Django 4.2.6 on 2023-10-25 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TravelApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plc', models.CharField(max_length=50, null=True)),
                ('dis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TravelApp.district')),
            ],
        ),
    ]
