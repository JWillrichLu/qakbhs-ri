from django.contrib import admin
from engine.admin import admin_site
from vosa.models import *
from django.utils.html import mark_safe


class aQAdmin(admin.TabularInline):
    model = AlternateQ
    list_display = ['id','question','main_qa', ]


class QAAdmin(admin.ModelAdmin):
    list_display = ['id','qakb', 'question','answer', 'n_aq']
    list_filter = ['qakb','qakb__kind']
    inlines = [aQAdmin]

admin_site.register(QA, QAAdmin)


class QAInline(admin.TabularInline):
    model = QA

class QAKBAdmin(admin.ModelAdmin):
    list_display = ['id','kind','name', 'n_qa', 'qrcode']
    list_filter = ['kind',]
    inlines = [QAInline]
    def qrcode(self,obj):
        return mark_safe('''<img src="https://api.qrserver.com/v1/create-qr-code/?data=%(data)s" alt="QAKB QRCode" title="Scan this to load %(target)s  onto your VOSAC." />''' % {  'data': obj.qakbqr_payload(), 'target': obj.name })
    qrcode.short_description = 'QRCODE'
    qrcode.allow_tags = True

admin_site.register(QAKB, QAKBAdmin)
