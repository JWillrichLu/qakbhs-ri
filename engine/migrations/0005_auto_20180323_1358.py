# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 13:58
from __future__ import unicode_literals

import ckeditor_uploader.fields
import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_auto_20180323_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsOverride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('tag', models.TextField(blank=True, editable=False, null=True)),
                ('site_accent_color', colorfield.fields.ColorField(default=b'#78a63e', max_length=18)),
                ('site_about', ckeditor_uploader.fields.RichTextUploadingField(default=b'Welcome! Enjoy it while we build it!', help_text=b'What you put here, will be shown to the public, to allow them to know what this website is about')),
            ],
            options={
                'verbose_name': 'Global Override Settings',
                'verbose_name_plural': 'Global Override Settings',
            },
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Global Settings', 'verbose_name_plural': 'Global Settings'},
        ),
    ]
