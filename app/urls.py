from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.base, name='base'),
    path('destinations/', views.destinations, name='destinations'),
    path('detailed_destination/', views.detailed_destination, name='detailed_destination'),
    path('add_destination/', views.add_destination, name='add_destination'),
]
