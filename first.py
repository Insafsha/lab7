import requests

def fetch_weather(city):
    api_key = "a9d02180fb9b946d96cb3149c3d15fba"
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}&lang=ru"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        weather_data = {
            "Описание погоды": data["weather"][0]["description"],
            "Температура воздуха": f"{data['main']['temp']}°C",
            "Ощущаемая температура": f"{data['main']['feels_like']}°C",
            "Процент влажности": f"{data['main']['humidity']}%",
            "Атмосферное давление": f"{data['main']['pressure']} гПа"
        }
        
        for param, info in weather_data.items():
            print(f"{param}: {info}")
    else:
        print(f"Ошибка запроса: {response.status_code}")
        print(f"Ответ сервера: {response.text}")

if __name__ == "__main__":
    fetch_weather("Surgut")