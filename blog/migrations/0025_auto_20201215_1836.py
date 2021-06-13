# Generated by Django 3.1 on 2020-12-15 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20201123_0802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='blogimages',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Settings', 'verbose_name_plural': 'Settings'},
        ),
    ]
