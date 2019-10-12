# Generated by Django 2.2.5 on 2019-09-28 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_link', models.URLField(verbose_name='Website Link')),
                ('title', models.CharField(max_length=35, verbose_name='Title')),
                ('description', models.TextField(max_length=100, verbose_name='Description')),
                ('reward_per_click', models.FloatField(verbose_name='Reward per click')),
                ('time_duration', models.DurationField(verbose_name='Time duration')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('question_type', models.CharField(choices=[('RA', 'Radio'), ('SE', 'Select')], max_length=2)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad_source.Task')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad_source.Question')),
            ],
        ),
    ]
