#from datetime import datetime
from django.utils.datetime_safe import datetime
from django.utils.timezone import now
from django import forms
from django.db import models

CHOICES= [
    ('-----','-----'),
    ('savings', 'Savings account'),
    ('current', 'Current account'),
    ('depoit', 'Depoit account'),
    ('demat', 'Demat account'),
    ]

GENDER_CHOICES = [('-----','-----'),('M','Male'),('F','Female')]


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100,null=True, blank=False)
    dob=models.DateTimeField(auto_now_add=True,null=True,blank=False)
    age=models.IntegerField(blank=False,null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='----')
    phone=models.IntegerField(blank=False,null=True)

    email=models.EmailField(max_length=100,blank=False,null=True)
    address=models.CharField(max_length=100,blank=False,null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=False, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=False, null=True)

    account_type=models.CharField(max_length=10, choices=CHOICES, default='----')


    credit_card=models.BooleanField(default=True)
    debit_card = models.BooleanField(default=False)
    pass_book = models.BooleanField(default=False)
    check_book = models.BooleanField(default=False)



    def __str__(self):
        return self.name