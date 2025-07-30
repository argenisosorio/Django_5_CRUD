from django.urls import path
from . import views

urlpatterns = [
    # Main route
    path('', views.home, name='home'),
]