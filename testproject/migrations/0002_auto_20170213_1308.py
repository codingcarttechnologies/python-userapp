# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-13 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='birthday',
            field=models.DateField(),
        ),
    ]
