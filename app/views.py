from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def destinations(request):
    return render(request, 'destinations.html')

def detailed_destination(request):
    return render(request, 'detailed_destination.html')

def add_destination(request):
    return render(request, 'add_destination.html')