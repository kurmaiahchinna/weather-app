import requests
from django.shortcuts import render


def index(request):
    weather_data = {}
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = '06916d2d0cda4ffbbdb6daeca49c8ebe'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.ok:
            data = response.json()
            weather_data = {
                'city': f"{data['name']}, {data['sys']['country']}",
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed'],
            }
        else:
            weather_data = {'error': 'City not found. Please try again.'}
    return render(request, 'testapp/weather.html', {'weather': weather_data})
