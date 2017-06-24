# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def bikes(request):
    print "Got here to view.py in bikes app ", "*"*50
    return render(request, 'bikes/index.html')