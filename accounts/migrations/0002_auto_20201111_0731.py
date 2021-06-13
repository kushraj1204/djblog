# Generated by Django 3.1.2 on 2020-11-11 01:46

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='longitude',
        ),
        migrations.AddField(
            model_name='customuser',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=django_google_maps.fields.AddressField(max_length=200, null=True),
        ),
    ]
