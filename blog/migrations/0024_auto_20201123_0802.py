# Generated by Django 3.1.2 on 2020-11-23 02:17

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20201122_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('alias', models.SlugField(max_length=200, unique=True)),
                ('fulltext', tinymce.models.HTMLField(null=True)),
                ('metakey', models.TextField(blank=True, null=True, verbose_name='Meta Key')),
                ('metadesc', models.TextField(blank=True, null=True, verbose_name='Meta Description')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='category',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='privacy_policy',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='terms_and_conditions',
        ),
        migrations.AddField(
            model_name='settings',
            name='metadesc',
            field=models.TextField(blank=True, null=True, verbose_name='Homepage Meta Description'),
        ),
        migrations.AddField(
            model_name='settings',
            name='metakey',
            field=models.TextField(blank=True, null=True, verbose_name='Homepage Meta Key'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='cat_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='displayphoto',
            field=models.ImageField(blank=True, null=True, upload_to='blog/static/blog', verbose_name='Display Photo'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='fulltext',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Full Text'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='introtext',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Intro Text'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='metadesc',
            field=models.TextField(blank=True, null=True, verbose_name='Meta Description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='metakey',
            field=models.TextField(blank=True, null=True, verbose_name='Meta Key'),
        ),
        migrations.AlterField(
            model_name='category',
            name='metadesc',
            field=models.TextField(blank=True, verbose_name='Meta Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='metakey',
            field=models.TextField(blank=True, verbose_name='Meta Key'),
        ),
    ]