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
#####второе задание
import requests
import json

def get_word_definition(word):
    api_key = "38d8ea98-913b-48cd-9965-d650f748b123"
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if isinstance(data, list) and data and isinstance(data[0], dict):
            definitions = data[0].get("shortdef", ["Нет определения"])
            part_of_speech = data[0].get("fl", "Не указано")
            pronunciation = data[0].get("hwi", {}).get("prs", [{}])[0].get("mw", "Не указано")
            
            examples = []
            if "def" in data[0]:
                senses = data[0]["def"][0].get("sseq", [])
                for sense in senses:
                    if isinstance(sense, list) and len(sense) > 0 and isinstance(sense[0], list):
                        dt = sense[0][1].get("dt", [])
                        for item in dt:
                            if item[0] == "text":
                                examples.append(item[1])
            
            print(f"Слово: {word}")
            print(f"Часть речи: {part_of_speech}")
            print(f"Произношение: {pronunciation}")
            print("Определения:")
            for idx, definition in enumerate(definitions, 1):
                print(f"  {idx}. {definition}")
            
            if examples:
                print("Примеры использования:")
                for example in examples:
                    print(f"  - {example}")
            else:
                print("Примеры не найдены.")
        else:
            print("Слово не найдено в словаре.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")

if __name__ == "__main__":
    word = input("Введите слово для поиска: ").strip()
    if word:
        get_word_definition(word)
    else:
        print("Ошибка: введите корректное слово.")


        #доп задание
import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def get_fox():
    response = requests.get("https://randomfox.ca/floof/")
    return response.json().get("image") if response.status_code == 200 else None

def update_image():
    image_url = get_fox()
    if image_url:
        response = requests.get(image_url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content)).resize((400, 400), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img

root = tk.Tk()
root.title("Случайная лиса")
root.geometry("450x500")
image_label = tk.Label(root)
image_label.pack()
tk.Button(root, text="Новая лиса!", command=update_image, font=("Arial", 14)).pack(pady=10)
update_image()
root.mainloop()
