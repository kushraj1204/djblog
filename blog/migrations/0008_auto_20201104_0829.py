# Generated by Django 3.1.2 on 2020-11-04 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='BlogImages',
        ),
    ]
