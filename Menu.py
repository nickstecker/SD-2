import os
import json
from User import User
from Translator import Translator
from Admin import Admin

class Menu():

    def showUserMenu(self, userTyp, userName):
        print("\n**************** BENUTZER-MENÜ ****************")
        print("Hey, " + userName + " was möchtest du machen?")
        print("(1) Nach einem Wort und dessen Übersetzungen suchen\n(2) Summer der angelegten Wörter anzeigen\n"
              "(3) Summer der Wörter in der Datenbank anzeigen\n(4) Programm beenden")
        userMenuNumber = int(input("-> Was möchtest du machen? "))
        if userMenuNumber == 1:
            Menu.searchWord(self, userTyp, userName)
        elif userMenuNumber == 2:
            User.showCreatedWordSum(self, userTyp, userName)
        elif userMenuNumber == 3:
            Menu.showSumWords(self, userTyp, userName)
        elif userMenuNumber == 4:
            print("Programm beendet!")

    def showTranslatorMenu(self, userTyp, translatorName):
        print("\n**************** ÜBERSETZER-MENÜ ****************")
        print("Hey, " + translatorName + " was möchtest du machen?")
        print("(1) Nach einem Wort und dessen Übersetzungen suchen\n(2) Summer der angelegten Wörter anzeigen\n"
              "(3) Summer der Wörter in der Datenbank anzeigen\n(4) Wörter anzeigen bei denen Übersetzungen fehlen\n"
              "(5) Programm beenden")
        translatorMenuNumber = int(input("-> Was möchtest du machen? "))
        if translatorMenuNumber == 1:
            Menu.searchWord(self, userTyp, translatorName)
        elif translatorMenuNumber == 2:
            Translator.showCreatedWordSum(self, userTyp, translatorName)
        elif translatorMenuNumber == 3:
            Menu.showSumWords(self, userTyp, translatorName)
        elif translatorMenuNumber == 4:
            print("4")
        elif translatorMenuNumber == 5:
            print("Programm beendet!")

    def showAdminMenu(self, userTyp, adminName):
        print("\n**************** ADMIN-MENÜ ****************")
        print("Hey, " + adminName + " was möchtest du machen?")
        print("(1) Nach einem Wort und dessen Übersetzungen suchen\n(2) Summer der angelegten Wörter anzeigen\n"
              "(3) Summer der Wörter in der Datenbank anzeigen\n(4) Wörter anzeigen bei denen Übersetzungen fehlen\n"
              "(5) Neue Sprache anlegen\n(6) Einem Übersetzer eine neue Sprache zuweisen\n(7) Programm beenden")
        adminMenuNumber = int(input("-> Was möchtest du machen? "))
        if adminMenuNumber == 1:
            Menu.searchWord(self, userTyp, adminName)
        elif adminMenuNumber == 2:
            Admin.showCreatedWordSum(self, userTyp, adminName)
        elif adminMenuNumber == 3:
            Menu.showSumWords(self, userTyp, adminName)
        elif adminMenuNumber == 4:
            print("Hi")
        elif adminMenuNumber == 5:
            print("Hi")
        elif adminMenuNumber == 6:
            print("Hi")
        elif adminMenuNumber == 7:
            print("Programm beendet!")

    def searchWord(self, userTyp, userName):
        print("Welches Wort willst du suchen?")
        wordToSearch = input("-> ")
        with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'r', encoding="utf-8") as file:
            wordData = json.load(file)
            translatedWords = []
            for word in wordData['words']:
                translatedWords.append(word['word'])
                if wordToSearch == word['word']:
                    print("Die Übersetzungen von " + wordToSearch + ":")
                    for translations in word['translations']:
                        for translation in translations:
                            if len(translations[translation]) != 0:
                                print(" -> " + translation + ": " + translations[translation])
                            else:
                                print(" -> " + translation + ": (keine)")
                    Menu.menuOrClose(self, userTyp, userName)
            if wordToSearch not in translatedWords:
                print("Das Wort " + wordToSearch + " ist noch nicht angelegt worden.")
                wantCreateWord = input("Möchtest du es anlegen? ja/nein\n-> ")
                if wantCreateWord == "ja":
                    Menu.createWord(self, wordToSearch, wordData, userName, userTyp)
                else:
                    Menu.menuOrClose(self, userTyp, userName)

    def createWord(self, wordToCreate, wordData, userName, userTyp):
        languages = {}
        for word in wordData['words']:
            id = word['id'] + 1
        for key in wordData['words'][0]['translations'][0].items():
            language = key[0]
            languages[language] = ""
        newWord = {'id': id, 'word': wordToCreate, 'translations': []}
        newWord['translations'].append(languages)
        wordData['words'].append(newWord)
        with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'w', encoding="utf-8") as file:
            json.dump(wordData, file, indent=4, ensure_ascii=False)
        print(wordToCreate + " wurde angelegt.")
        Menu.increaseCreatedWords(self, userTyp, userName)

    def increaseCreatedWords(self, userTyp, userName):
        if userTyp == 1:
            with open(os.path.join(os.path.dirname(__file__), 'UserDatabase.json'), 'r', encoding="utf-8") as f:
                userData = json.load(f)
            with open(os.path.join(os.path.dirname(__file__), 'UserDatabase.json'), 'w', encoding="utf-8") as f:
                for user in userData['users']:
                    if user['benutzername'] == userName:
                        user['angelegteWörter'] += 1
                json.dump(userData, f, indent=4, ensure_ascii=False)
        if userTyp == 2:
            with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'r', encoding="utf-8") as f:
                translatorData = json.load(f)
            with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'w', encoding="utf-8") as f:
                for translator in translatorData['translators']:
                    if translator['benutzername'] == userName:
                        translator['angelegteWörter'] += 1
                json.dump(translatorData, f, indent=4, ensure_ascii=False)
        if userTyp == 3:
            with open(os.path.join(os.path.dirname(__file__), 'AdminDatabase.json'), 'r', encoding="utf-8") as f:
                adminData = json.load(f)
            with open(os.path.join(os.path.dirname(__file__), 'AdminDatabase.json'), 'w', encoding="utf-8") as f:
                for admin in adminData['admins']:
                    if admin['benutzername'] == userName:
                        admin['angelegteWörter'] += 1
                json.dump(adminData, f, indent=4, ensure_ascii=False)
        Menu.menuOrClose(self, userTyp, userName)

    def showSumWords(self, userTyp, userName):
        with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'r', encoding="utf-8") as file:
            wordData = json.load(file)
            for word in wordData['words']:
                sumWords = word['id']
        print("Die Summe der Wörter in der Datenbank: " + str(sumWords))
        Menu.menuOrClose(self, userTyp, userName)

    def menuOrClose(self, userTyp, userName):
        print("\nWas möchtest du jetzt machen?")
        print("(1) Zurück zum Hauptmenü\n(2) Programm beenden")
        menuOrClose = int(input("-> "))
        if menuOrClose == 1 and userTyp == 1:
            Menu.showUserMenu(self, userTyp, userName)
        elif menuOrClose == 1 and userTyp == 2:
            Menu.showTranslatorMenu(self, userTyp, userName)
        elif menuOrClose == 1 and userTyp == 3:
            Menu.showAdminMenu(self, userTyp, userName)
        else:
            print("Programm beendet!")