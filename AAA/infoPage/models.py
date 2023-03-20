from django.db import models

class support (models.Model):
    firstName = models.CharField()
    lastName = models.CharField()
    fatherName = models.CharField()
    fastDesc = models.CharField()
    price = models.IntegerField()
    consultType = models.CharField()

class job (models.Model):
    jobTitle = models.CharField()
    jobPrice = models.IntegerField()
    expeirence = models.BooleanField()
    region = models.CharField()
    jobCategory = models.CharField()

class user (models.Model):
    firstName = models.CharField()
    lastName = models.CharField()
    fatherName = models.CharField()
    userCity = models.CharField()
    userEmail = models.EmailField()
    userPassword = models.CharField()
