from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('tourist-destinations/', TouristDestinationCreateView.as_view(), name='tourist-destination-list-create'),
    path('tourist-destinations-detail/<int:pk>/', TouristDestinationDetailView.as_view(), name='tourist-destinations-detail'),
    path('tourist-destinations-delete/<int:pk>/', DeleteTouristDestination.as_view(), name='tourist-destinations-delete'),
    
    
    path('create/', views.create_tourist_destination, name='add_destination'),
    path('', views.base, name='base'),
    path('destinations/', views.destinations, name='destinations'),
    path('update_destination/<int:pk>/', views.update_destination, name='update_destination'),
    path('detailed_destination/<int:pk>/', views.detailed_destination, name='detailed_destination'),
    path('delete_destination/<int:pk>/', views.delete_destination, name='delete_destination'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#imp for what you want to achieve.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)