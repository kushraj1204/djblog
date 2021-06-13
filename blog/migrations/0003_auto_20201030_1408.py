# Generated by Django 3.1.2 on 2020-10-30 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20201030_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='modified_by',
            field=models.ForeignKey(db_column='modified_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
