import json
import os
from UserFactory import User_Factory
import re

class Login():

    def login():
        print("\n")
        print("**************** LOGIN ****************")
        print("(1) Benutzer\n(2) Übersetzer\n(3) Admin")
        print("Mit wem willst du dich anmelden?")
        userTyp = input("Gebe die zahl ein -> ")

        if re.search("[a-zA-ZäÄüÜöÖ]", userTyp):
            print("Du hast ein Buchstabe eingegeben. Gebe bitte eine Zahl von 1-3 ein.")
            Login.login()
        elif int(userTyp) == 1:
            print("\nGebe deinen Benutzernamen ein")
            userName = input("Benutzernamen: ")
            with open(os.path.join(os.path.dirname(__file__), 'UserDatabase.json'), 'r', encoding="utf-8") as file:
                userData = json.load(file)
                if userName == userData['users'][0]["username"]:
                    print("Erfolgreich eingelogt")
                    user = User_Factory.getUserTyp('user', userName)
                    user.showMenu(int(userTyp), userName)
                else:
                    print("Benutzername oder Passwort falsch")
                    Login.login()
        elif int(userTyp) == 2:
            print("\nGib dein Benutzernamen und dein Passwort ein")
            translatorName = input("Benutzernamen: ")
            translatorPassword = input("Passwort: ")
            with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'r', encoding="utf-8") as file:
                translatorData = json.load(file)
                if translatorName == translatorData['translators'][0]['username'] and translatorPassword == \
                        translatorData['translators'][0]['password']:
                    print("Erfolgreich eingelogt")
                    translator = User_Factory.getUserTyp('translator', translatorName)
                    translator.showMenu(int(userTyp), translatorName)
                else:
                    print("Benutzername oder Passwort falsch")
                    Login.login()
        elif int(userTyp) == 3:
            print("\nGib dein Benutzernamen und dein Passwort ein")
            adminName = input("Benutzernamen: ")
            adminPassword = input("Passwort: ")
            with open(os.path.join(os.path.dirname(__file__), 'AdminDatabase.json'), 'r', encoding="utf-8") as file:
                adminData = json.load(file)
                if adminName == adminData['admins'][0]['username'] and adminPassword == adminData['admins'][0][
                    'password']:
                    print("Erfolgreich eingelogt")
                    admin = User_Factory.getUserTyp('admin', adminName)
                    admin.showMenu(int(userTyp), adminName)
                else:
                    print("Benutzername oder Passwort falsch")
                    Login.login()
        else:
            print("Du hast eine flasche Zahl eingegeben. Bitte gebe eine Zahl von 1-3 ein.")
            Login.login()