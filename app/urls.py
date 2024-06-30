from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('tourist-destinations/', TouristDestinationCreateView.as_view(), name='tourist-destination-list-create'),
    
    
    path('create/', views.create_tourist_destination, name='add_destination'),
    path('', views.base, name='base'),
    path('destinations/', views.destinations, name='destinations'),
    path('detailed_destination/', views.detailed_destination, name='detailed_destination'),
  
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#imp for what you want to achieve.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)