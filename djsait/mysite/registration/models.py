from django.db import models

class Rasp(models.Model):
    data = models.DateField()
    urok1 = models.CharField(max_length=30)
    urok2 = models.CharField(max_length=30)
    urok3 = models.CharField(max_length=30)
    urok4 = models.CharField(max_length=30)
    urok5 = models.CharField(max_length=30)
    urok6 = models.CharField(max_length=30)


