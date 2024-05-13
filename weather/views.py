import requests

from django.shortcuts import render

def index(request):
    API_KEY = None
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    if request.method == "POST":
        city1 = request.POST["city1"]
        

        weather_data1= fetch_weather_and_forecast(city1, API_KEY, current_weather_url)
    
        

        context = {
                "weather_data1": weather_data1,
              
            }

        return render(request, "weather_app/index.html", context)
    
    else:
        return render(request, "weather_app/index.html")
    

def fetch_weather_and_forecast(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response['coord']['lon']

    weather_data = {
        "city": city,
        "temperature" : round(response['main']['temp']-273.15, 2),
        "description" : response['weather'][0]['description'],
        "icon": response['weather'][0]['icon']
    }

    return weather_data
