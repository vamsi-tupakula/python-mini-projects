import requests
import json
import random

def get_random_word():
    response_API = requests.get('https://www.randomlists.com/data/words.json')
    data = response_API.text
    json_data = json.loads(data)
    words = json_data["data"]

    return random.choice(words)

random_word = get_random_word()
print(random_word)