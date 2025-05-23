import requests

API_KEY = '5b0b761c57d477309c859005da2770b0'  # Replace with your OpenWeatherMap API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    """Fetch weather data for a given city."""
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return parse_weather_data(data)
    else:
        return f"Error: {response.status_code}, {response.text}"

def parse_weather_data(data):
    """Parse the weather data from the API response."""
    city = data['name']
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    
    return {
        'city': city,
        'temperature': temperature,
        'description': weather_description
    }

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    print(weather)