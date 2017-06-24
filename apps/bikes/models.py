# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#pylint: disable=E1101,C0111,C0103
# Create your models here.

class UserManager(models.Manager):
    def addreviewval(self, postdata):
        results = {'status':True, 'errors':[]}
        if not postdata['model'] or len(postdata['model']) < 3:
            results['errors'].append("Bike Model: 3 or more chars")
            results['status'] = False
        if postdata['newmake']:
            print "New Make Detected","*"*50
            #DB push new Make
        print "New Make Detected","*"*50
        # user = User.objects.filter(email=postdata['email'])
        # if user:
        #     results['status'] = False
        #     results['errors'].append("User already exists. Please login...")
        # if results['status']:
        #     userpassword = bcrypt.hashpw(postdata['userpassword'].encode(), bcrypt.gensalt())
        # insertbikereview = bikereview.objects.create(
        #     modelyear=postdata['modelyear'],
        #     make=postdata['first_name'],
        #     model=postdata['last_name'],
        #     email=postdata['email'],
        #     userpassword=userpassword)
        # results['user'] = user
        return results

class BikeMake(models.Model):
    make = models.CharField(max_length=255)
    #BikeModels

class BikeReview(models.Model):
    make = models.ForeignKey(BikeMake, related_name="BikeModels")
    model = models.CharField(max_length=255)
    modelyear = models.IntegerField
    review = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id + "," + self.model
    objects = UserManager()


