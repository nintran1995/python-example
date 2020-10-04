from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Boarding 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    model = Boarding
    template_name = 'bookings/index.html'


def search(request, boarding_zip_code, boarding_start, boarding_end, boarding_size):
    return HttpResponse("You're looking at question %s." % boarding_zip_code)