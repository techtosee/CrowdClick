# Generated by Django 2.2.5 on 2019-10-12 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad_source', '0003_blank_description'),
    ]

    operations = [
        migrations.RenameModel('Advertisement', 'Task'),
        migrations.RenameField('Question', 'ad', 'task'),
    ]
