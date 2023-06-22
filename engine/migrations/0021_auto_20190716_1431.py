# Generated by Django 2.2.3 on 2019-07-16 14:31

import ckeditor_uploader.fields
import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import engine.models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0020_homepagesettings_show_welcome_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='child_of',
            field=models.ForeignKey(blank=True, help_text='Under which category should this one be nested?', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_children', to='engine.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='on_menu',
            field=models.BooleanField(default=False, help_text='If set, then this category will have an entry on the categories menu', verbose_name='On Menu?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='on_nav',
            field=models.BooleanField(default=False, help_text='If set, then this category will have an entry on the navigation bar', verbose_name='On Nav?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(1, 'FIRST'), (2, 'SECOND'), (3, 'THIRD'), (4, 'FOURTH'), (5, 'FIFTH')], default=1, help_text='A category with a high priority will have its content having a higher visibility precendence than others. FIRST is the highest.'),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='accent_color',
            field=colorfield.fields.ColorField(default='#78a63e', max_length=18),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='card_columns',
            field=models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=3, help_text='How many card columns to show per row?'),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='fore_color',
            field=colorfield.fields.ColorField(default='#dddddd', max_length=18),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='show_welcome_message',
            field=models.BooleanField(default=True, help_text='If set, then the welcome message below will be rendered on the Home page', verbose_name='Show Welcome?'),
        ),
        migrations.AlterField(
            model_name='homepagesettings',
            name='welcome_message',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Welcome! Enjoy it while we build it!', help_text='Default message on the home page/landing page.'),
        ),
        migrations.AlterField(
            model_name='page',
            name='accent_color',
            field=colorfield.fields.ColorField(default='#000', max_length=18),
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.ForeignKey(help_text='Under which category should this page be nested?', on_delete=django.db.models.deletion.CASCADE, related_name='my_pages', to='engine.Category'),
        ),
        migrations.AlterField(
            model_name='page',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='The summary or brief of the contents of this page -- used on preview tiles', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='on_landing',
            field=models.BooleanField(default=True, help_text='If set, then this page will show up on the default landing page', verbose_name='On Landing?'),
        ),
        migrations.AlterField(
            model_name='page',
            name='on_nav',
            field=models.BooleanField(default=False, help_text='If set, then this page will have an entry on the navigation menu', verbose_name='On Nav?'),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_icon',
            field=models.ImageField(blank=True, help_text='This image will act as the page icon in navigation and on preview uis', null=True, upload_to=engine.models.page_icon_upload_to),
        ),
        migrations.AlterField(
            model_name='page',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(1, 'FIRST'), (2, 'SECOND'), (3, 'THIRD'), (4, 'FOURTH'), (5, 'FIFTH')], default=1, help_text='A page with a high priority will have its content having a higher visibility precendence than others. FIRST is the highest.'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='card_columns',
            field=models.PositiveSmallIntegerField(choices=[(1, 'ONE'), (2, 'TWO'), (3, 'THREE'), (4, 'FOUR'), (5, 'FIVE')], default=3, help_text='On grid pages, how many card columns to show per row?'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='categories_title',
            field=models.CharField(default='Categories', max_length=20, verbose_name='Categories Title'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='site_about',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Welcome! This Site is Still Under Construction', help_text='What you put here, will be shown to the public, to allow them to know what this website is about'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='site_accent_color',
            field=colorfield.fields.ColorField(default='#78a63e', max_length=18),
        ),
        migrations.AlterField(
            model_name='settings',
            name='site_fore_color',
            field=colorfield.fields.ColorField(default='#dddddd', max_length=18),
        ),
        migrations.AlterField(
            model_name='settings',
            name='site_name',
            field=models.CharField(default='Site Under Construction', max_length=32),
        ),
    ]
