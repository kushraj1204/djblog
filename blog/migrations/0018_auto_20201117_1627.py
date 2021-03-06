# Generated by Django 3.1.2 on 2020-11-17 10:42

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20201111_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='displayphoto',
            field=models.ImageField(blank=True, null=True, upload_to='blog/static/blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='fulltext',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='introtext',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='metadata',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='metadesc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='metakey',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='research_data',
            field=tinymce.models.HTMLField(default='Research Data'),
        ),
    ]
