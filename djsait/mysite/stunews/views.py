from django.shortcuts import render
from .models import News


def stunews_func(request):

    gavno = News.objects.all()
    return render(request, 'stunews/base.html', {'gavno': gavno})
