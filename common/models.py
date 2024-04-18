from django.db import models
from django.contrib.auth.models import AbstractUser

import datetime

class Country(models.Model):
    country = models.CharField(max_length=100, null=True, blank=True, default='中国')
    id = models.BigAutoField(primary_key=True)

class CustomUser(AbstractUser):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    sn = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

class Order(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    create_date = models.DateTimeField(default=datetime.datetime.now)
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    medicines = models.ManyToManyField('Medicine', through='OrderMedicine')

class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()

from django.contrib import admin

admin.site.register(Country)
admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(OrderMedicine)



