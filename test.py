import os
import json

with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'r', encoding="utf-8") as file:
    wordData = json.load(file)
    for word in wordData['words']:
        print(word)
        for translations in word['translations']:
            print(translations)