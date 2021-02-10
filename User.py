import UserTyp
import Menu

class User(UserTyp):

    def __init__(self, userId, userName, userMenu):
        self.userId = userId
        self.userName = userName
        self.userMenu = userMenu

    def showMenu(self):
        Menu.showUserMenu()

    def searchWord(self):
        print("hi")

    def createWord(self):
        print("hi")

    def showCreatedWordSum(self):
        with open(os.path.join(os.path.dirname(__file__), 'UserDatabase.json'), 'r', encoding="utf-8") as file:
            createdWords = json.load(file)
            print("Die Summer deiner angelegten Wörter ist: " + str(createdWords['user'][0]['angelegteWörter']))