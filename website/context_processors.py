import logging
from website.settings import BASE_URL, STATIC_URL, APP_NAME, POWERED_BY, LOG_LEVEL, MAIN_LOG
from engine.models import Settings, Category, Page


logging.basicConfig(level=LOG_LEVEL, filename=MAIN_LOG)
logger = logging.getLogger(__name__)


def extras(request):
    stuff = {
        'BASE_URL': BASE_URL,
        'STATIC_URL': STATIC_URL,
        'APP_NAME': APP_NAME,
        'POWERED_BY': POWERED_BY,
        'gsettings': Settings.get_settings(),
        'categories': Category.objects.all(),
        'cpages': Page.objects.all(),
    }

    if request.user.is_authenticated:
        stuff['user'] = request.user
        try:
            profile = request.user.profile
            stuff['DATAADMIN_ACCOUNT'] = profile.data_admin
        except:
            pass
    return stuff
