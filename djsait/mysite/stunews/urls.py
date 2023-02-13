from django.urls import path
from stunews import views
urlpatterns = [
    path('', views.stunews_func, name='stunewspage'),
]