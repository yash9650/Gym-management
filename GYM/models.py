from django.db import models


# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=10,primary_key=True)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    date = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    amount = models.CharField(max_length=20)
    duraton = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=10,primary_key=True)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10,default=False)
    plan = models.CharField(max_length=10)
    joindate = models.CharField(max_length=20)
    expiredate = models.CharField(max_length=20)
    initalamount = models.CharField(max_length=20)

    def __str__(self):
        return self.name
