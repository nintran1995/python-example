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
    # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # return HttpResponse("You're looking at question %s." % boarding_zip_code)
    boardings = Boarding.objects.filter(
        size=boarding_size).order_by('-start_date')[:5]
    return render(request, 'bookings/search.html', {
        'boardings': boardings,
    })
