import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metrics&lang=es&APPID=076e9519efb070c5ddf4e3b5a1e3d6ba'
    err = False
    #city = 'Saltillo,Mx'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    try:
        err = False
        for city in cities:

            r = requests.get(url.format(city)).json()

            celsius = r['main']['temp'] - 273
            celsius = round(celsius, 1)
            temp_max = r['main']['temp_max'] - 273
            temp_max = round(temp_max, 1)
            temp_min = r['main']['temp_min'] - 273
            temp_min = round(temp_min, 1)

            city_weather = {
                'city': city.name,
                'temperature': celsius,
                'tempMax': temp_max,
                'tempMin': temp_min,
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }

            weather_data.append(city_weather)
    except KeyError:
        pass
    except Exception as e:
        pass

    print(weather_data)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'Clima/Clima2.html', context)
