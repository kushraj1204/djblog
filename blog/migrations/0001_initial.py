# Generated by Django 3.1.2 on 2020-10-30 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.IntegerField(blank=True, default=0)),
                ('right', models.IntegerField(blank=True, default=0)),
                ('level', models.IntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=200)),
                ('alias', models.CharField(max_length=200)),
                ('note', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('checked_out_at', models.DateTimeField(auto_now=True)),
                ('metadesc', models.TextField(blank=True)),
                ('metakey', models.TextField(blank=True)),
                ('metadata', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('checked_out_by', models.ForeignKey(db_column='checked_out_by', on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_checked_out_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(db_column='modified_by', on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_modified_by', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('alias', models.CharField(max_length=200, unique=True)),
                ('introtext', models.CharField(max_length=200)),
                ('fulltext', tinymce.models.HTMLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('checked_out_time', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False)),
                ('metakey', models.TextField(blank=True)),
                ('metadesc', models.TextField(blank=True)),
                ('hits', models.IntegerField(blank=True)),
                ('metadata', models.TextField(blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.category')),
                ('checked_out_by', models.ForeignKey(db_column='checked_out_by', on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_checked_out_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(db_column='modified_by', on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]