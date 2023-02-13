from django.urls import path
from registration import views
urlpatterns = [
    path('', views.main_student, name='mainpage'),
]