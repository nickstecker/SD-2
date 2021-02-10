import UserTyp
import Menu

class Translator(UserTyp):

    def __init__(self, translatorId, translatorName, translatorMenu):
        self.translatorId = translatorId
        self.translatorName = translatorName
        self.translatorMenu = translatorMenu

    def showMenu(self):
        Menu.showTranslatorMenu()