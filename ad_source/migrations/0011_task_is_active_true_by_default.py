# Generated by Django 2.2.10 on 2020-02-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_source', '0010_task_og_image_null_and_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
