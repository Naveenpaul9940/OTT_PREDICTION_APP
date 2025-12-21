from django.urls import path
from .views import dropoff

urlpatterns = [
    path('', dropoff, name='predict'),
]