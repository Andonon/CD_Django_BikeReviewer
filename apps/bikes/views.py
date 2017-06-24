# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BikeReview
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def bikes(request):
    return render(request, 'bikes/index.html')

def newreview(request):
    return render(request, 'bikes/newreview.html')

def insertreview(request):
    print "Got here to addreview in view.py in bikes app ", "*"*50
    print request.POST
    newreviewsend = BikeReview.objects.addreviewval(request.POST)
    return redirect('/bikes')
