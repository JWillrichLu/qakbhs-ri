from django.conf.urls import url, include
from django.contrib import admin
from engine import views as v
from engine.admin import admin_site
from vosa import views as vv

import adminactions.actions as actions

# register all adminactions
actions.add_to_site(admin_site)

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^about/$', v.about, name='about'),
    url(r'^category/(?P<cid>\d+)/', v.category, name='category'),
    url(r'^page/(?P<pid>\d+)/', v.page, name='page'),
    url(r'^admin/', admin_site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),


    url(r'^api/qakb/(?P<tid>\d+)/', vv.jqakb, name='jqakb'),
    url(r'^api/qakb/(?P<tid>\d+)/qrcode/', vv.jqakb, name='jqakbqr'),

     url(r'^adminactions/', include('adminactions.urls')),
]
