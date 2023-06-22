from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from vosa.models import QAKB
from website.settings import LOG_DIR, MAIN_LOG, LOG_LEVEL, BASE_URL
import logging


logging.basicConfig(level=LOG_LEVEL, filename=MAIN_LOG)
logger = logging.getLogger(__name__)

@csrf_exempt
def jqakb(request, tid):
    qakb = None
    try:
        qakb = QAKB.objects.get(pk=tid)
    except:
        return HttpResponse( "NOT FOUND", status = 404)

    return HttpResponse(qakb.to_json(), status=200)

