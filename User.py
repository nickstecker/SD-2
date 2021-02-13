import os
import json
from UserTyp import UserTyp
import Menu

class User(UserTyp):

    def __init__(self, userName):
        self.userName = userName

    def showMenu(self, userTyp, userName):
        Menu.Menu.showUserMenu(self, userTyp, userName)

    def showCreatedWordSum(self, userTyp, userName):
        with open(os.path.join(os.path.dirname(__file__), 'UserDatabase.json'), 'r', encoding="utf-8") as file:
            userData = json.load(file)
            for user in userData['users']:
                if user['username'] == userName:
                    createdWords = user['createdWords']
            print("\nDas ist die Summer deiner angelegten Wörter:")
            print("-> " + str(createdWords))
        Menu.Menu.menuOrClose(self, userTyp, userName)