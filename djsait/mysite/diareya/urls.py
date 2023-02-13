from django.urls import path
from diareya import views
urlpatterns = [
    path('', views.diareya_view, name='diareya'),
]