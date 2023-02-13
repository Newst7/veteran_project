from django.shortcuts import render
from .models import Marks
from .models import diary_rasp1
from .models import diary_rasp2
from .models import diary_rasp3
from .models import diary_rasp4
from .models import diary_rasp5
from .models import diary_rasp6
# Create your views here.

def diareya_view (request):
    content = {
        'day1': diary_rasp1.objects.all(),
        'day2': diary_rasp2.objects.all(),
        'day3': diary_rasp3.objects.all(),
        'day4': diary_rasp4.objects.all(),
        'day5': diary_rasp5.objects.all(),
        'day6': diary_rasp6.objects.all(),
        'marks': Marks.objects.all(),
    }

    return render(request, 'diareya/diary.html', {'content': content})