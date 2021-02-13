import os
import json
from UserTyp import UserTyp
import Menu

class Admin(UserTyp):

    def __init__(self, adminName):
        self.adminName = adminName

    def showMenu(self, userTyp, adminName):
        Menu.Menu.showAdminMenu(self, userTyp, adminName)

    def showCreatedWordSum(self, userTyp, adminName):
        with open(os.path.join(os.path.dirname(__file__), 'AdminDatabase.json'), 'r', encoding="utf-8") as file:
            adminData = json.load(file)
            for user in adminData['admins']:
                if user['username'] == adminName:
                    createdWords = user['createdWords']
            print("\nDas ist die Summer deiner angelegten Wörter:")
            print("-> " + str(createdWords))
        Menu.Menu.menuOrClose(self, userTyp, adminName)

    def showTranslatedWords(self, userTyp, adminName):
        with open(os.path.join(os.path.dirname(__file__), 'AdminDatabase.json'), 'r', encoding="utf-8") as file:
            adminData = json.load(file)
            for admin in adminData['admins']:
                if admin['username'] == adminName:
                    translatedWords = admin['translatedWords']
            print("\nDas ist die Summer deiner selbst übersetzten Wörter:")
            print("-> " + str(translatedWords))
        Menu.Menu.menuOrClose(self, userTyp, adminName)