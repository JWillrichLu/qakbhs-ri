from django.shortcuts import render
import logging
from engine.models import Category, Page, Settings, HomePageSettings
from website.settings import BASE_URL, STATIC_URL, APP_NAME, LOG_LEVEL, MAIN_LOG


logging.basicConfig(level=LOG_LEVEL, filename=MAIN_LOG)
logger = logging.getLogger(__name__)


def home(request):
    settings = None
    try:
        settings = HomePageSettings.objects.latest('id')
    except BaseException as e:
        pass
    categories = None
    try:
        categories = Category.objects.all()
    except BaseException as e:
        pass
    pages = None
    try:
        pages = Page.objects.filter(on_landing=True)
    except BaseException as e:
        pass
    ctx = {
            'settings': settings,
            'categories': categories,
            'pages': pages
            }
    return render(request, 'website/index.html', ctx)

def about(request):
    settings = None
    try:
        settings = Settings.objects.latest('id')
    except:
        pass
    categories = None
    try:
        categories = Category.objects.all()
    except:
        pass
    ctx = {
            'title': 'ABOUT %s' % settings.site_name,
            'settings': settings,
            'categories': categories,
            }
    return render(request, 'website/about.html', ctx)

def category(request, cid):
    settings = None
    try:
        settings = Settings.objects.latest('id')
    except:
        pass
    cat = None
    try:
        cat = Category.objects.get(id=cid)
    except:
        pass
    pages = None
    try:
        pages = Page.objects.filter(category__id=cid)
    except:
        pass
    ctx = {
            'title': cat,
            'category': cat,
            'pages': pages
            }
    return render(request, 'website/category.html', ctx)


def page(request, pid):
    page = None
    try:
        page = Page.objects.get(id=pid)
    except:
        pass
    ctx = {
            'title': page.title,
            'page': page
            }
    return render(request, 'website/page.html', ctx)
