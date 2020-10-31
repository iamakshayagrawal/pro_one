from django.urls import path
from .views import app_two

urlpatterns = [
    path('', app_two, name='app_two'),
]