import os
import json
from UserTyp import UserTyp
import Menu

class Translator(UserTyp):

    def __init__(self, translatorName):
        self.translatorName = translatorName

    def showMenu(self, userTyp, translatorName):
        Menu.Menu.showTranslatorMenu(self, userTyp, translatorName)

    def showCreatedWordSum(self, userTyp, translatorName):
        with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'r', encoding="utf-8") as file:
            translatorData = json.load(file)
            for translator in translatorData['translators']:
                if translator['username'] == translatorName:
                    createdWords = translator['createdWords']
            print("\nDas ist die Summer deiner angelegten Wörter:")
            print("-> " + str(createdWords))
        Menu.Menu.menuOrClose(self, userTyp, translatorName)

    def showTranslatedWords(self, userTyp, translatorName):
        with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'r', encoding="utf-8") as file:
            translatorData = json.load(file)
            for translator in translatorData['translators']:
                if translator['username'] == translatorName:
                    translatedWords = translator['translatedWords']
            print("\nDas ist die Summer deiner selbst übersetzten Wörter:")
            print("-> " + str(translatedWords))
        Menu.Menu.menuOrClose(self, userTyp, translatorName)
