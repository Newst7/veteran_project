from django.db import models

class News(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=15)
    fam = models.CharField(max_length=25)
    otch = models.CharField(max_length=25)
    url_photo = models.CharField(max_length=255)
    news_data = models.DateField()
