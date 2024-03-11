from django.urls import path
from . import views

urlpatterns = [
    path('', views.weekdays, name='weekdays'),
]
