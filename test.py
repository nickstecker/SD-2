import os
import json

print("Wörter bei denen Übersetzungen fehlen:")

with open(os.path.join(os.path.dirname(__file__), 'language.json'), 'r', encoding="utf-8") as file:
    languageData = json.load(file)
    for language in languageData['languages']:
        languageId = language['id'] - 1

with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'r', encoding="utf-8") as file:
    wordData = json.load(file)
    for word in wordData['words']:
        sumWords = word['id']
        for translations in word['translations']:
            countMissTrans = 0
            for translation in translations:
                if len(translations[translation]) == 0:
                    countMissTrans += 1
        if countMissTrans > 0:
            missingTrans = 100 - ((countMissTrans / languageId) * 100)
            print("-> " + word['word'] + " " + "(" + str(missingTrans) + " % übersetzt)")