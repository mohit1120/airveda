# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-03 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('temp', models.CharField(max_length=10)),
                ('startDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
