from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
import datetime

def hello(request):
      return HttpResponse("Hello world")

def current_datetime(request):
    current_date_time = datetime.datetime.now()
    return render_to_response('dateapp/current_time.html', locals())

def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('dateapp/hours_ahead.html', locals())