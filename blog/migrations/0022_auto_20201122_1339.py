# Generated by Django 3.1.2 on 2020-11-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20201122_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='authored',
            field=models.BooleanField(default=False, verbose_name='Authoring completed'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='edited',
            field=models.BooleanField(default=False, verbose_name='Editing completed'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='researched',
            field=models.BooleanField(default=False, verbose_name='Research completes'),
        ),
    ]
