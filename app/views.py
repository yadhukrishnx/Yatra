from django.shortcuts import render,redirect
import requests
from .models import TouristDestination
from .serializers import TouristDestinationSerializer
from .forms import TouristDestinationForm
from django.contrib import messages
from rest_framework import generics
from rest_framework.permissions import AllowAny
# Create your views here.


class TouristDestinationCreateView(generics.ListCreateAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer
    permission_classes = [AllowAny]

class TouristDestinationDetailView(generics.ListAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer
    
class DeleteTouristDestination(generics.DestroyAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer



def create_tourist_destination(request):
    if request.method == 'POST':
        place_name = request.POST.get('place_name')
        weather = request.POST.get('weather')
        state = request.POST.get('state')
        district = request.POST.get('district')
        google_map_link = request.POST.get('google_map_link')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        if place_name and weather and state and district and google_map_link and description :
            try:
                # Create a new TouristDestination instance and save it to the database
                destination = TouristDestination(
                    place_name=place_name,
                    weather=weather,
                    state=state,
                    district=district,
                    google_map_link=google_map_link,
                    description=description,
                    image=image
                )
                destination.save()
                
                # Prepare data for the API request
                api_url = 'http://127.0.0.1:8000/tourist-destinations/'
                data = {
                    'place_name': place_name,
                    'weather': weather,
                    'state': state,
                    'district': district,
                    'google_map_link': google_map_link,
                    'description': description
                }
                files = {'image': image}
                
                # Send POST request to the API
                response = requests.post(api_url, data=data, files=files)
                
                if response.status_code == 400:  # HTTP 201 Created
                    messages.success(request, 'Tourist Destination Inserted Successfully')
                    return redirect('add_destination')
                else:
                    messages.error(request, f'Error {response.status_code}: {response.text}')
            except requests.RequestException as e:
                messages.error(request, f'Error during API request: {str(e)}')
        else:
            messages.error(request, 'All fields are required')
    return render(request, 'add_destination.html')



def update_destination(request, pk):
    api_url = f'http://127.0.0.1:8000/tourist-destinations-detail/{pk}/'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        destination_instance = TouristDestination.objects.get(pk=pk)

        
        

        if request.method == 'POST':
            form = TouristDestinationForm(request.POST, request.FILES, instance=destination_instance)
            if form.is_valid():
                form.save()
                messages.success(request, 'Destination details updated successfully.')
                return redirect('update_destination', pk=pk)  # Redirect to update page on success
            else:
                messages.error(request, 'Error updating destination details. Please check the form.')
        else:
            form = TouristDestinationForm(instance=destination_instance)

        return render(request, 'update_destination.html', {'form': form, 'destinationdata': destination_instance, 'destinations': destinations})

    # Handle error cases if the API request fails
    messages.error(request, 'Failed to fetch destination details.')
    return redirect('home')  # Redirect to home or any other page on API request failure








def base(request):
    destinations = TouristDestination.objects.all()
    return render(request, 'base.html',{'destinations': destinations})

def destinations(request):
    destinations = TouristDestination.objects.all()
    return render(request, 'destinations.html',{'destinations': destinations})

def detailed_destination(request, pk):
    api_url = f'http://127.0.0.1:8000/tourist-destinations-detail/{pk}/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        destination_instance = TouristDestination.objects.get(pk=pk)
    
    return render(request, 'detailed_destination.html',{'destination': destination_instance})

# def add_destination(request):
#     return render(request, 'add_destination.html')


def delete_destination(request, pk):
    api_url = f'http://127.0.0.1:8000/tourist-destinations-delete/{pk}'

    response = requests.delete(api_url)

    if response.status_code == 200:
        messages.success(request, 'Destination details updated successfully.')
        
    else:
        print(f'Failed to delete item. Status code {response.status_code}')

    return redirect('destinations')