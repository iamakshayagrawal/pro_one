from django.urls import path
from .views import app_three

urlpatterns = [
    path('', app_three, name='app_three'),
]