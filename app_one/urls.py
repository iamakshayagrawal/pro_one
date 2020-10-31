from django.urls import path
from .views import app_one

urlpatterns = [
    path('', app_one, name='app_one'),
]