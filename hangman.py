from tokenize import String
import requests
import json
import random
import string

def get_random_word():
    # fetching api
    response_API = requests.get('https://www.randomlists.com/data/words.json')
    data = response_API.text

    # coverting it into json
    json_data = json.loads(data)
    words = json_data["data"]

    return random.choice(words).upper()

def hangman():
    word = get_random_word()
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    user_letters = set() # letters entered by user

    while(len(word_letters) > 0):
        print('You have used : ', ' '.join(user_letters))

        word_list = [letter if letter in user_letters else '-' for letter in word]
        print('current word : ', " ".join(word_list))

        user_letter = input('Guess an alphabet : ').upper()
        if user_letter in alphabets - user_letters:
            user_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in user_letters:
            print('you have already used it..')
        else:
            print("You entered a invalid char...")

    print('final word : ', " ".join(word))    


hangman()