# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-04 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0008_remove_creator_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='name',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]