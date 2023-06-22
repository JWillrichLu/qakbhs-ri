# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 08:36
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0013_auto_20180330_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagesettings',
            name='fore_color',
            field=colorfield.fields.ColorField(default=b'#dddddd', max_length=18),
        ),
        migrations.AlterField(
            model_name='settings',
            name='site_fore_color',
            field=colorfield.fields.ColorField(default=b'#dddddd', max_length=18),
        ),
    ]
