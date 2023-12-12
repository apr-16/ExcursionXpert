# Generated by Django 4.2.6 on 2023-10-27 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TravelApp', '0004_rename_disid_places_dis'),
    ]

    operations = [
        migrations.CreateModel(
            name='packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packages_name', models.CharField(max_length=50, null=True)),
                ('destination', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=50, null=True)),
                ('cost', models.CharField(max_length=50, null=True)),
                ('inclusions', models.CharField(max_length=50, null=True)),
                ('attraction', models.CharField(max_length=50, null=True)),
                ('more_info', models.CharField(max_length=50, null=True)),
                ('images1', models.FileField(max_length=50, null=True, upload_to='')),
                ('images2', models.FileField(max_length=50, null=True, upload_to='')),
                ('images3', models.FileField(max_length=50, null=True, upload_to='')),
                ('dis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TravelApp.district')),
            ],
        ),
        migrations.DeleteModel(
            name='places',
        ),
    ]