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
