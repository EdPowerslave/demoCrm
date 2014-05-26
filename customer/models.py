# -*- coding: utf-8 -*-

from django.db import models
from django import forms
from django.forms.extras.widgets import SelectDateWidget

class Customer(models.Model):
    name = models.CharField('name', editable=True, max_length="50")
    surname = models.CharField('surname', max_length="50")
    birth_date=models.DateField()
    email = models.EmailField(max_length=70,blank=True, null=True, unique= True)
    country = models.CharField('country', max_length="50")
    city = models.CharField('city', max_length="50")
    address = models.CharField('address', max_length="100")
    home_phone = models.IntegerField('home phone')
    mobile_phone = models.IntegerField('mobile phone ')
    added = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name + " " + self.surname



class Meeting(models.Model):
    Ziyaret = 'Ziyaret'
    Telefon1 = 'Telefon(Biz Aradık)'
    Telefon2 = 'Telefon(Aradı)'

    TYPE_CHOICES =((Ziyaret,'Ziyaret'),(Telefon2,'Telefon(Aradı)'),(Telefon1,'Telefon(Biz Aradık)'))

    Yapitasi_Residence = 'YT Residence'
    Yapitasi_Life = 'YT Life'

    PROJECT_CHOICES = ((Yapitasi_Residence,'YT Residence'),(Yapitasi_Life,'YT Life'))

    customer = models.ForeignKey(Customer)
    meeting_type = models.CharField(max_length="20", choices=TYPE_CHOICES, default=Ziyaret)
    meeting_date = models.DateTimeField(auto_now=True)
    meeting_project = models.CharField(max_length="20", choices=PROJECT_CHOICES, default=Yapitasi_Residence)
    meeting_comment = models.TextField('meeting comments', max_length="50")

    def __unicode__(self):
        return "Meeting {0} of {1}".format(self.meeting_type, self.customer)


