# Generated by Django 5.0.9 on 2024-09-17 16:22

import dream.content_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=dream.content_app.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=dream.content_app.models.upload_to)),
            ],
        ),
    ]
