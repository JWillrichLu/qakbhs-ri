from django import template
import logging
from website.settings import BASE_URL, STATIC_URL, APP_NAME, POWERED_BY, LOG_LEVEL, MAIN_LOG


logging.basicConfig(level=LOG_LEVEL, filename=MAIN_LOG)
logger = logging.getLogger(__name__)

register = template.Library()

@register.filter
def modulo0(num, val):
    #logger.error("num:%s, val:%s" % (num, val))
    a= (int(num) % int(val))==0
    #logger.error("%s %% %s == 0 : %s" % (num, val, a))
    return a
