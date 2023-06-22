from django.db import models
from django.urls import reverse
from website.settings import LOG_LEVEL, MAIN_LOG, DOMAIN
import logging
from colorfield.fields import ColorField
from ckeditor_uploader.fields import RichTextUploadingField
from singleton_models.models import SingletonModel
import uuid
import os
import datetime

logging.basicConfig(level=LOG_LEVEL, filename=MAIN_LOG)
logger = logging.getLogger(__name__)

#------------------------------------------------
# UTILS, you know..
#------------------------------------------------

def page_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('%s/%s' % (datetime.date.today().strftime('page_images%Y/%m/%d'), filename))


def page_icon_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('%s/%s' % (datetime.date.today().strftime('page_icons%Y/%m/%d'), filename))



def site_logo_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('%s/%s' % (datetime.date.today().strftime('site_logos%Y/%m/%d'), filename))

# end UTILS.
#------------------------------------------------


#------------------------------------------------
# Constants and Magic stuff...
#------------------------------------------------

class PRIORITY_INDEX:
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    CHOICES = (
            (FIRST, 'FIRST'),
            (SECOND, 'SECOND'),
            (THIRD, 'THIRD'),
            (FOURTH, 'FOURTH'),
            (FIFTH, 'FIFTH'),
            )


class COLUMNS:
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    CHOICES = (
            (ONE,'ONE'),
            (TWO,'TWO'),
            (THREE,'THREE'),
            (FOUR,'FOUR'),
            (FIVE,'FIVE'),
            )



# end Constants.
#------------------------------------------------

#------------------------------------------------
# MODELS and model mechanics
#------------------------------------------------

class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tag = models.TextField(editable=False, null=True, blank=True)

    name = models.CharField(max_length=20)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_INDEX.CHOICES, default = PRIORITY_INDEX.FIRST, help_text="A category with a high priority will have its content having a higher visibility precendence than others. FIRST is the highest.")
    on_nav = models.BooleanField(default=False, help_text="If set, then this category will have an entry on the navigation bar", verbose_name="On Nav?")
    on_menu = models.BooleanField(default=False, help_text="If set, then this category will have an entry on the categories menu", verbose_name="On Menu?")
    child_of = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='my_children', help_text="Under which category should this one be nested?", blank=True, null=True)

    @property
    def on_main_menu(self):
        if not self.on_menu:
            return False
        return True if self.child_of is None else False

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['priority']


class Page(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tag = models.TextField(editable=False, null=True, blank=True)

    title = models.CharField(max_length=100)
    #description = models.TextField(null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True, help_text='The summary or brief of the contents of this page -- used on preview tiles')
    cover_image = models.ImageField(upload_to=page_image_upload_to, null=True, blank=True)
    page_icon = models.ImageField(upload_to=page_icon_upload_to, null=True, blank=True, help_text='''This image will act as the page icon in navigation and on preview uis''')
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_INDEX.CHOICES, default = PRIORITY_INDEX.FIRST, help_text="A page with a high priority will have its content having a higher visibility precendence than others. FIRST is the highest.")
    on_nav = models.BooleanField(default=False, help_text="If set, then this page will have an entry on the navigation menu", verbose_name="On Nav?")
    on_landing = models.BooleanField(default=True, help_text="If set, then this page will show up on the default landing page", verbose_name="On Landing?")
    #content = RichTextUploadingField ()
    content = RichTextUploadingField ()
    accent_color = ColorField(default='#000')
    override_css = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='my_pages', help_text="Under which category should this page be nested?")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority','-id','-created']



class Settings(SingletonModel):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tag = models.TextField(editable=False, null=True, blank=True)

    site_name = models.CharField(max_length=32, default="Site Under Construction")
    site_brand_image = models.ImageField(upload_to=site_logo_image_upload_to, null=True, blank=True)
    site_fore_color = ColorField(default='#dddddd')
    site_accent_color = ColorField(default='#78a63e')
    site_about = RichTextUploadingField (help_text="What you put here, will be shown to the public, to allow them to know what this website is about", default="Welcome! This Site is Still Under Construction")
    categories_title = models.CharField(max_length=20, default="Categories", verbose_name='Categories Title')
    card_columns = models.PositiveSmallIntegerField(choices=COLUMNS.CHOICES, default = COLUMNS.THREE, help_text="On grid pages, how many card columns to show per row?")

    @staticmethod
    def get_settings():
        try:
            if Settings.objects.all().count() == 0:
                '''create the default settings'''
                try:
                    Settings().save()
                except:
                    pass
            return Settings.objects.latest('id')
        except:
            return None # esp. before migrate db is run

    def __str__(self):
        return u"Global Settings" # something like this will make admin message strings more coherent

    class Meta:
        verbose_name = "Global Settings" # once again this will make sure your admin UI doesn't have illogical text
        verbose_name_plural = "Global Settings"



class HomePageSettings(SingletonModel):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tag = models.TextField(editable=False, null=True, blank=True)

    fore_color = ColorField(default='#dddddd')
    accent_color = ColorField(default='#78a63e')
    show_welcome_message = models.BooleanField(default=True, help_text="If set, then the welcome message below will be rendered on the Home page", verbose_name="Show Welcome?")
    welcome_message = RichTextUploadingField (help_text="Default message on the home page/landing page.", default="Welcome! Enjoy it while we build it!")
    card_columns = models.PositiveSmallIntegerField(choices=COLUMNS.CHOICES, default = COLUMNS.THREE, help_text="How many card columns to show per row?")

    def __str__(self):
        return u"Home Page Settings" # something like this will make admin message strings more coherent

    class Meta:
        verbose_name = "Home Page Settings" # once again this will make sure your admin UI doesn't have illogical text
        verbose_name_plural = "Home Page Settings"
