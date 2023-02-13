from django.shortcuts import render
from .models import Rasp

def main_student(request):
    rasp_data = Rasp.objects.all()
    return render(request, 'registration/main.html', {'rasp_data':rasp_data})