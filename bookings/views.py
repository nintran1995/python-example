from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Boarding 

def index(request):
    template = loader.get_template('bookings/index.html')
    return HttpResponse(template.render({}, request))