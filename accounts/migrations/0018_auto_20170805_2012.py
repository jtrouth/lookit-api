# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-05 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20170805_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographicdata',
            name='additional_comments',
            field=models.TextField(blank=True),
        ),
    ]