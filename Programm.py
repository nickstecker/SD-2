import json
import os
from UserFactory import User_Factory
from User import User
from Menu import Menu
from Translator import Translator
from Admin import Admin

def login():
    print("\n")
    print("**************** LOGIN ****************")
    print("(1) Benutzer\n(2) Übersetzer\n(3) Admin")
    userTyp = int(input("-> Wer bist du? "))

    if userTyp == 1:
        print("\nGebe deinen Benutzernamen ein")
        userName = input("Benutzernamen: ")
        with open(os.path.join(os.path.dirname(__file__), 'UserDatabase.json'), 'r', encoding="utf-8") as file:
            userData = json.load(file)
            if userName == userData['users'][0]["benutzername"]:
                print("Erfolgreich eingelogt")
                user = User_Factory.getUserTyp('user', userName)
                user.showMenu(userTyp, userName)
            else:
                print("Benutzername oder Passwort falsch")
                login()
    elif userTyp == 2:
        print("\nGib dein Benutzernamen und dein Passwort ein")
        translatorName = input("Benutzernamen: ")
        translatorPassword = input("Passwort: ")
        with open(os.path.join(os.path.dirname(__file__), 'TranslatorDatabase.json'), 'r', encoding="utf-8") as file:
            translatorData = json.load(file)
            if translatorName == translatorData['translators'][0]['benutzername'] and translatorPassword == translatorData['translators'][0]['passwort']:
                print("Erfolgreich eingelogt")
                translator = User_Factory.getUserTyp('translator', translatorName)
                translator.showMenu(userTyp, translatorName)
            else:
                print("Benutzername oder Passwort falsch")
                login()
    elif userTyp == 3:
        print("\nGib dein Benutzernamen und dein Passwort ein")
        adminName = input("Benutzernamen: ")
        adminPassword = input("Passwort: ")
        with open(os.path.join(os.path.dirname(__file__), 'AdminDatabase.json'), 'r', encoding="utf-8") as file:
            adminData = json.load(file)
            if adminName == adminData['admins'][0]['benutzername'] and adminPassword == adminData['admins'][0]['passwort']:
                print("Erfolgreich eingelogt")
                admin = User_Factory.getUserTyp('admin', adminName)
                admin.showMenu(userTyp, adminName)
            else:
                print("Benutzername oder Passwort falsch")
                login()
    else:
        print("Du hast eine flasche Zahl eingegeben.")
        login()


if __name__ == "__main__":
        login()