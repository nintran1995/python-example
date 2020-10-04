from django.conf.urls import url
from . import views

app_name = "bookings"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<boarding_zip_code>[a-zA-Z0-9!@#\$%\^\&*\)\(+=._-]+)/(?P<boarding_start>[a-zA-Z0-9!@#\$%\^\&*\)\(+=._-]+)/(?P<boarding_end>[a-zA-Z0-9!@#\$%\^\&*\)\(+=._-]+)/(?P<boarding_size>[a-zA-Z0-9!@#\$%\^\&*\)\(+=._-]+)/$', views.search, name='search'),
]
