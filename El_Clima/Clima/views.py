import requests
from django.shortcuts import render

def index(request):
    url = 'https://api.darksky.net/forecast/af08feb858612b09132c8f531f1bd340/25.4333,-101' 
    city = 'Las Vegas'

    r = requests.get(url.format(city))
    print(r.text)
    return render(request, 'Clima/Clima.html')