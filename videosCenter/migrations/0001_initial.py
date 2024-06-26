# Generated by Django 5.0.3 on 2024-03-26 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=5000)),
                ('publishing_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('videos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumnails', to='videosCenter.videos')),
            ],
        ),
    ]
