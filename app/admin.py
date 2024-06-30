# admin.py

from django.contrib import admin
from .models import TouristDestination

@admin.register(TouristDestination)
class TouristDestinationAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'state', 'district')
    search_fields = ('place_name', 'state', 'district')
    # Add more customization as needed
