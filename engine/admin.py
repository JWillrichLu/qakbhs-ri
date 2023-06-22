#-- Django
from django.contrib import admin
#-- Other Contributions
from singleton_models.admin import SingletonModelAdmin
#-- Our Engine
from engine.forms import PageForm
from engine.models import Page, Category, Settings, HomePageSettings

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from website.settings import  APP_NAME
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin


class CustomAdminSite(AdminSite):
    settings = Settings.get_settings()
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('%s' % APP_NAME)

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('%s' % settings.site_name if settings is not None else APP_NAME)

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('%s Admin Dashboard' % settings.site_name if settings is not None else APP_NAME)

admin_site = CustomAdminSite()

# we'll need to register the default auth modules ourselves...
admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)


class PageAdmin(admin.ModelAdmin):
    form = PageForm
    list_display = ['title','view_page_icon','priority','on_nav', 'on_landing','category']
    list_editable = ['priority','on_nav','on_landing', 'category']
    def view_page_icon(self, obj):
        try:
            return '''<img style="width:1.5rem; height:1.5rem;" src="%(icon_url)s" />''' % {'icon_url': obj.page_icon.url }
        except:
            return ''
    view_page_icon.allow_tags = True
    view_page_icon.short_description = 'Icon'

admin_site.register(Page, PageAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','priority','on_nav', 'on_menu']
    list_editable = ['priority','on_nav','on_menu' ]

admin_site.register(Category, CategoryAdmin)

admin_site.register(Settings, SingletonModelAdmin)
admin_site.register(HomePageSettings, SingletonModelAdmin)
