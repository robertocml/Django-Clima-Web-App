import requests
from django.shortcuts import render

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metrics&lang=es&APPID=076e9519efb070c5ddf4e3b5a1e3d6ba'
    city = 'Monterrey,Mx'

    r = requests.get(url.format(city)).json()

    celsius = r['main']['temp'] - 273
    celsius = round(celsius,1)

    city_weather = {
        'city': city,
        'temperature': celsius ,
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather' : city_weather}

    return render(request, 'Clima/Clima.html',context)