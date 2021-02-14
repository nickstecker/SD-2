import os
import json
import User
import Translator
import Admin
import re

class Menu():

    def showUserMenu(self, userTyp, userName):
        print("\n**************** BENUTZER-MENÜ ****************")
        print("Hey, " + userName + " was möchtest du machen?")
        print("(1) Nach einem Wort und dessen Übersetzungen suchen\n(2) Summe der angelegten Wörter anzeigen\n"
              "(3) Summe der Wörter in der Datenbank anzeigen\n(4) Programm beenden")
        userMenuNumber = int(input("-> Was möchtest du machen? "))
        Menu.menuNavigation(self, userTyp, userName, userMenuNumber)

    def showTranslatorMenu(self, userTyp, translatorName):
        print("\n**************** ÜBERSETZER-MENÜ ****************")
        print("Hey, " + translatorName + " was möchtest du machen?")
        print("(1) Nach einem Wort und dessen Übersetzungen suchen\n(2) Summe der angelegten Wörter anzeigen\n"
              "(3) Summe der Wörter in der Datenbank anzeigen\n(4) Summe der selbst übersetzten Wörter anzeigen\n"
              "(5) Wörter anzeigen bei denen Übersetzungen fehlen\n(6) Programm beenden")
        translatorMenuNumber = int(input("-> Was möchtest du machen? "))
        Menu.menuNavigation(self, userTyp, translatorName, translatorMenuNumber)

    def showAdminMenu(self, userTyp, adminName):
        print("\n**************** ADMIN-MENÜ ****************")
        print("Hey, " + adminName + " was möchtest du machen?")
        print("(1) Nach einem Wort und dessen Übersetzungen suchen\n(2) Summe der angelegten Wörter anzeigen\n"
              "(3) Summer der Wörter in der Datenbank anzeigen\n(4) Wörter anzeigen bei denen Übersetzungen fehlen\n"
              "(5) Neue Sprache anlegen\n(6) Einem Übersetzer eine neue Sprache zuweisen\n(7) Programm beenden")
        adminMenuNumber = int(input("-> Was möchtest du machen? "))
        Menu.menuNavigation(self, userTyp, adminName, adminMenuNumber)

    def menuNavigation(self, userTyp, userName, menuNumber):
        if menuNumber == 1:
            Menu.searchWord(self, userTyp, userName)
        elif menuNumber == 2 and userTyp == 1:
            User.User.showCreatedWordSum(self, userTyp, userName)
        elif menuNumber == 2 and userTyp == 2:
            Translator.Translator.showCreatedWordSum(self, userTyp, userName)
        elif menuNumber == 2 and userTyp == 3:
            Admin.Admin.showCreatedWordSum(self, userTyp, userName)
        elif menuNumber == 3:
            Menu.showSumWords(self, userTyp, userName)
        elif menuNumber == 4 and userTyp == 1:
            print("Programm beendet!")
        elif menuNumber == 4 and userTyp == 2:
            Translator.Translator.showTranslatedWords(self, userTyp, userName)
        elif menuNumber == 4 and userTyp == 3:
            Menu.showListOfMissingTrans(self, userTyp, userName)
        elif menuNumber == 5 and userTyp == 1:
            Menu.invalidInput(self, userTyp, userName)
        elif menuNumber == 5 and userTyp == 2:
            Menu.showListOfMissingTrans(self, userTyp, userName)
        elif menuNumber == 5 and userTyp == 3:
            Menu.createNewLanguage(self, userTyp, userName)
        elif menuNumber == 6 and userTyp == 1:
            Menu.invalidInput(self, userTyp, userName)
        elif menuNumber == 6 and userTyp == 2:
            print("Programm beendet!")
        elif menuNumber == 6 and userTyp == 3:
            Menu.assignLanguageToTranslator(self, userTyp, userName)
        elif menuNumber == 7 and userTyp == 1:
            Menu.invalidInput(self, userTyp, userName)
        elif menuNumber == 7 and userTyp == 2:
            Menu.invalidInput(self, userTyp, userName)
        elif menuNumber == 7 and userTyp == 3:
            print("Programm beendent!")
        elif menuNumber > 7 or menuNumber < 1:
            Menu.invalidInput(self, userTyp, userName)

    def invalidInput(self, userTyp, userName):
        print("\nUngültige Eingabe - Versuche es nochmal!")
        if userTyp == 1:
            Menu.showUserMenu(self, userTyp, userName)
        elif userTyp == 2:
            Menu.showTranslatorMenu(self, userTyp, userName)
        elif userTyp == 3:
            Menu.showAdminMenu(self, userTyp, userName)

    def searchWord(self, userTyp, userName):
        print("\nWelches Wort willst du suchen?")
        wordToSearch = input("-> ")
        if re.search("[0-9]", wordToSearch):
            print("Ein Wort darf keine zahlen enthalten. Versuche es nochmal!")
            Menu.searchWord(self, userTyp, userName)
        else:
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
                    if user['username'] == userName:
                        user['createdWords'] += 1
                json.dump(userData, f, indent=4, ensure_ascii=False)
        if userTyp == 2:
            with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'r', encoding="utf-8") as f:
                translatorData = json.load(f)
            with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'w', encoding="utf-8") as f:
                for translator in translatorData['translators']:
                    if translator['username'] == userName:
                        translator['createdWords'] += 1
                json.dump(translatorData, f, indent=4, ensure_ascii=False)
        if userTyp == 3:
            with open(os.path.join(os.path.dirname(__file__), 'AdminDatabase.json'), 'r', encoding="utf-8") as f:
                adminData = json.load(f)
            with open(os.path.join(os.path.dirname(__file__), 'AdminDatabase.json'), 'w', encoding="utf-8") as f:
                for admin in adminData['admins']:
                    if admin['username'] == userName:
                        admin['createdWords'] += 1
                json.dump(adminData, f, indent=4, ensure_ascii=False)
        Menu.menuOrClose(self, userTyp, userName)

    def showSumWords(self, userTyp, userName):
        with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'r', encoding="utf-8") as file:
            wordData = json.load(file)
            sumWords = 0
            countEmptyWords = 0
            for word in wordData['words']:
                sumWords = word['id']
                for translations in word['translations']:
                    for translation in translations:
                        if len(translations[translation]) == 0:
                            countEmptyWords += 1
                            break
            completeTransWord = sumWords - countEmptyWords
        print("\nDie Summe der Wörter in der Datenbank: " + str(sumWords))
        if completeTransWord == 1:
            print("Davon ist " + str(completeTransWord) + " Wort zu 100% übersetzt")
        else:
            print("Davon sind " + str(completeTransWord) + " Wörter zu 100% übersetzt")
        Menu.menuOrClose(self, userTyp, userName)

    def showListOfMissingTrans(self, userTyp, userName):
        print("\nDas sind die Wörter bei denen Übersetzungen fehlen:")
        with open(os.path.join(os.path.dirname(__file__), 'language.json'), 'r', encoding="utf-8") as file:
            languageData = json.load(file)
            for language in languageData['languages']:
                languageId = language['id'] - 1
        with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'r', encoding="utf-8") as file:
            wordData = json.load(file)
            for word in wordData['words']:
                for translations in word['translations']:
                    countMissTrans = 0
                    for translation in translations:
                        if len(translations[translation]) == 0:
                            countMissTrans += 1
                if countMissTrans > 0:
                    missingTrans = 100 - ((countMissTrans / languageId) * 100)
                    print("-> " + word['word'] + " " + "(" + str(missingTrans) + " % übersetzt)")
        if userTyp == 2:
            Menu.getWordsToTranslate(self, userTyp, userName)
        else:
            Menu.menuOrClose(self, userTyp, userName)

    def increaseTransWords(self, userTyp, userName):
        with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'r', encoding="utf-8") as f:
            translatorData = json.load(f)
        with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'w', encoding="utf-8") as f:
            for translator in translatorData['translators']:
                if translator['username'] == userName:
                    translator['translatedWords'] += 1
            json.dump(translatorData, f, indent=4, ensure_ascii=False)
        Menu.menuOrClose(self, userTyp, userName)

    def createNewLanguage(self, userTyp, userName):
        print("\nWelche Sprache möchtest du anlegen?")
        languageToCreate = input("-> ")
        languageId = 0
        languages = []
        with open(os.path.join(os.path.dirname(__file__), 'language.json'), 'r', encoding="utf-8") as file:
            languageData = json.load(file)
            file.close()
        for language in languageData['languages']:
            languageId = language['id'] + 1
            languages.append(language["languagename"])
        if languageToCreate in languages:
            print("Die Sprache " + '"' + languageToCreate + '"' + " wurde schon angelegt")
            print("Möchtest du eine andere Sprache anlegen? ja/nein")
            if input("-> ") == "ja":
                Menu.createNewLanguage(self, userTyp, userName)
            else:
                Menu.menuOrClose(self, userTyp, userName)
        else:
            newLanguage = {"id": languageId, "languagename": languageToCreate}
            languageData['languages'].append(newLanguage)
            with open(os.path.join(os.path.dirname(__file__), 'language.json'), 'w', encoding="utf-8") as file:
                json.dump(languageData, file, indent=4, ensure_ascii=False)
                file.close()
            print("Die Sprache " + '"' + str(languageToCreate) + '"' + " wurde erfolgreich angelegt")
            Menu.assignNewLanguageToWordDatabase(self, userTyp, userName, languageToCreate)

    def assignNewLanguageToWordDatabase(self, userTyp, userName, newLanguage):
        with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'r', encoding="utf-8") as file:
            wordData = json.load(file)
        for word in wordData["words"]:
            languages = {}
            for translations in word["translations"]:
                languages = translations
            languages[newLanguage] = ""
            with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'w', encoding="utf-8") as file:
                json.dump(wordData, file, indent=4, ensure_ascii=False)
        Menu.menuOrClose(self, userTyp, userName)

    def assignLanguageToTranslator(self, userTyp, userName):
        print("\nWem möchtest du eine neue Sprache zuweisen?")
        translatorName = input("-> ")
        usernames = []
        with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'r', encoding="utf-8") as file:
            translatorData = json.load(file)
            for translator in translatorData["translators"]:
                usernames.append(translator["username"])
        if translatorName in usernames:
            print("Welche Sprache möchtest du " + translatorName + " zuweisen?")
            languageToAssign = input("-> ")
            languagenames = {}
            with open(os.path.join(os.path.dirname(__file__), 'language.json'), 'r', encoding="utf-8") as file:
                languageData = json.load(file)
                for languages in languageData['languages']:
                    languagenames[languages['languagename']] = languages['id']
            if languageToAssign in languagenames:
                for translator in translatorData['translators']:
                    if translatorName == translator["username"]:
                        translatorAssignedLang = []
                        for languages in translator["assignedLanguages"]:
                            translatorAssignedLang.append(languages["languagename"])
                        if languageToAssign in translatorAssignedLang:
                            print(translatorName + " wurde die Sprache " + '"' + languageToAssign + '"' + " schon zugewiesen")
                            Menu.menuOrClose(self, userTyp, userName)
                        else:
                            newTranslatorLanguage = {"languageId": languagenames[languageToAssign],
                                                     "languagename": languageToAssign}
                            with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'r',
                                      encoding="utf-8") as file:
                                translatorData = json.load(file)
                            for translator in translatorData["translators"]:
                                if translatorName == translator['username']:
                                    translator['assignedLanguages'].append(newTranslatorLanguage)
                            with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'w',encoding="utf-8") as file:
                                json.dump(translatorData, file, indent=4, ensure_ascii=False)
                            print(
                                "Die Sprache " + '"' + languageToAssign + '"' + " wurde " + translatorName + " zugewiesen")
                            Menu.menuOrClose(self, userTyp, userName)
            else:
                print("Diese Sprache ist noch nicht angelegt worden")
                print("Willst du die Sprache anlegen? ja/nein")
                assignLanguage = input("-> ")
                if assignLanguage == "ja":
                    Menu.createNewLanguage(self, userTyp, userName)
                elif assignLanguage == "nein":
                    Menu.menuOrClose(self, userTyp, userName)
        else:
            print("Diesen Übersetzer gibt es nicht")
            Menu.menuOrClose(self, userTyp,userName)

    def getWordsToTranslate(self, userTyp, userName):
        print("\nMöchtest du eines dieser Wörter übersetzen? ja/nein")
        if input("-> ") == "ja":
            with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'r',
                      encoding="utf-8") as file:
                tranlatorData = json.load(file)
            for translator in tranlatorData["translators"]:
                if "translator" == translator["username"]:
                    entitledLanguages = []
                    for language in translator["assignedLanguages"]:
                        entitledLanguages.append(language["languagename"])
            with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'r', encoding="utf-8") as file:
                wordData = json.load(file)
            print("\nDas sind deine Möglichkeiten:")
            wordCount = 1
            wordList = {}
            for word in wordData["words"]:
                counter = 0
                for translations in word["translations"]:
                    for translation in translations:
                        if translations[translation] == "" and translation in entitledLanguages and counter == 0:
                            wordList[word["word"]] = []
                            wordList[word["word"]].append(translation)
                            print("(" + str(wordCount) + ")" + "Du kannst " + '"' + word["word"] + '"' + ":")
                            print(" -> auf " + translation + " übersetzen")
                            counter += 1
                            wordCount += 1
                        elif translations[translation] == "" and translation in entitledLanguages:
                            print(" -> auf " + translation + " übersetzen")
                            wordList[word["word"]].append(translation)
            Menu.translateWords(self, userTyp, userName, wordList)
        else:
            Menu.menuOrClose(self, userTyp, userName)

    def translateWords(self, userTyp, userName, wordList):
        print("\nWelches Wort willst du übersetzten?")
        wordToTranslate = input("-> ")
        if wordToTranslate in wordList:
            print("In welcher Sprache willst du " + '"' + wordToTranslate + '"' + " übersetzen?(Sprache bitte auf Englisch eingeben)")
            language = input("-> ")
            if language in wordList[wordToTranslate]:
                print("\nBitte gebe die Übersetzung von " + '"' + wordToTranslate + '"' + " auf " + language + " ein:")
                translation = input("Übersetzung: ")
                with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'r', encoding="utf-8") as file:
                    wordData = json.load(file)
                for word in wordData["words"]:
                    if wordToTranslate == word["word"]:
                        for translations in word["translations"]:
                            translations[language] = translation
                with open(os.path.join(os.path.dirname(__file__), 'WordDatabase.json'), 'w', encoding="utf-8") as file:
                    json.dump(wordData, file, indent=4, ensure_ascii=False)
                print("Die Übersetzung wurde aktualisiert")
                Menu.increaseTransWords(self, userTyp, userName)
            else:
                print(
                    '"' + wordToTranslate + '"' + " wurde entweder schon auf dieser Sprache übersetzt oder du hast keine Berechtigung "
                    + '"' + wordToTranslate + '"' + " auf dieser Sprache zu übersetzen")
                Menu.translateWords(self, userTyp, userName, wordList)
        else:
            print("Falsches Wort eingegeben")
            Menu.translateWords(self, userTyp, userName, wordList)

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
