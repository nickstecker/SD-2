import UserTyp
import Menu

class Admin(UserTyp):

    def __init__(self, adminId, adminName, adminMenu):
        self.adminId = adminId
        self.adminName = adminName
        self.adminMenu = adminMenu

    def showMenu(self):
        Menu.showAdminMenu()