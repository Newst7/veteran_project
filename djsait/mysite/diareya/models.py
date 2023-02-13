from django.db import models

class Marks(models.Model):
    ball = models.IntegerField()
    homework = models.TextField()
    url_task = models.CharField(max_length=250)
    data_task = models.DateField()
    predmet = models.CharField(max_length=20)

class diary_rasp1(models.Model):
    diary_urok1 = models.CharField(max_length=20)
    diary_urok2 = models.CharField(max_length=20)
    diary_urok3 = models.CharField(max_length=20)
    diary_urok4 = models.CharField(max_length=20)
    diary_urok5 = models.CharField(max_length=20)
    diary_urok6 = models.CharField(max_length=20)

class diary_rasp2(models.Model):
    diary_urok1 = models.CharField(max_length=20)
    diary_urok2 = models.CharField(max_length=20)
    diary_urok3 = models.CharField(max_length=20)
    diary_urok4 = models.CharField(max_length=20)
    diary_urok5 = models.CharField(max_length=20)
    diary_urok6 = models.CharField(max_length=20)

class diary_rasp3(models.Model):
    diary_urok1 = models.CharField(max_length=20)
    diary_urok2 = models.CharField(max_length=20)
    diary_urok3 = models.CharField(max_length=20)
    diary_urok4 = models.CharField(max_length=20)
    diary_urok5 = models.CharField(max_length=20)
    diary_urok6 = models.CharField(max_length=20)

class diary_rasp4(models.Model):
    diary_urok1 = models.CharField(max_length=20)
    diary_urok2 = models.CharField(max_length=20)
    diary_urok3 = models.CharField(max_length=20)
    diary_urok4 = models.CharField(max_length=20)
    diary_urok5 = models.CharField(max_length=20)
    diary_urok6 = models.CharField(max_length=20)

class diary_rasp5(models.Model):
    diary_urok1 = models.CharField(max_length=20)
    diary_urok2 = models.CharField(max_length=20)
    diary_urok3 = models.CharField(max_length=20)
    diary_urok4 = models.CharField(max_length=20)
    diary_urok5 = models.CharField(max_length=20)
    diary_urok6 = models.CharField(max_length=20)

class diary_rasp6(models.Model):
    diary_urok1 = models.CharField(max_length=20)
    diary_urok2 = models.CharField(max_length=20)
    diary_urok3 = models.CharField(max_length=20)
    diary_urok4 = models.CharField(max_length=20)
    diary_urok5 = models.CharField(max_length=20)
    diary_urok6 = models.CharField(max_length=20)