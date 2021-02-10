import Menu
import json
import UserTyp
import User
import Translator
import Admin


class User_Factory(UserTyp):
    @staticmethod
    def getUserTyp(type):
        if type == 'user':
            return User()
        if type == 'translator':
            return Translator()
        if type == 'admin':
            return Admin()

factory = User_Factory()
user1 = factory.getUserTyp('user')
user1.showMenu()