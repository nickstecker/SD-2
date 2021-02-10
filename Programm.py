import json
import os

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
            if userName == userData["user"][0]["benutzername"]:
                print("Erfolgreich eingelogt")
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
            else:
                print("Benutzername oder Passwort falsch")
                login()
    else:
        print("Du hast eine flasche Zahl eingegeben.")
        login()

    return userTyp


if __name__ == "__main__":
        login()