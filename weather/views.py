from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=43a4f460916426100aee3e38418d1e91').read()
        json_data = json.loads(res)
        temperature = int(round(json_data['main']['temp']))
        data = {
            "country_code": str(json_data['sys']['country']),
            "lon": str(json_data['coord']['lon']),
            "lat": str(json_data['coord']['lat']),
            "temp": str(temperature) + '°C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "temp_min": str(json_data['main']['temp_min'])+'k',
            "temp_max": str(json_data['main']['temp_max'])+'k',
            "wind_deg": str(json_data['wind']['deg']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})