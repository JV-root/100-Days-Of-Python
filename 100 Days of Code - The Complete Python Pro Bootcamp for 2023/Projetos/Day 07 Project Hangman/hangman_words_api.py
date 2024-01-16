import requests
import json

def get_words():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=100")
    word_list = response.json()
    return word_list
