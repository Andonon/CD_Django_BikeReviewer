''' App URLS.py file. '''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.bikes),
    url(r'^newreview$', views.newreview),
    url(r'^insertreview$', views.insertreview),
]
