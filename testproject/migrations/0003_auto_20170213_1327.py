# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-13 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0002_auto_20170213_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='birthday',
            field=models.DateTimeField(),
        ),
    ]
