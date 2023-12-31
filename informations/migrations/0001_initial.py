# Generated by Django 5.0 on 2023-12-13 20:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConcernLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=20)),
                ('speciality', models.CharField(max_length=20)),
                ('faculty', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=20)),
                ('campus', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('active', 'Active'), ('unvalid', 'Unvalid'), ('pending', 'Pending')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('concern_levels', models.ManyToManyField(to='informations.concernlevel')),
            ],
        ),
    ]
