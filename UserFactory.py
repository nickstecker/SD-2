import Menu
import json
from UserTyp import UserTyp
from User import User
from Translator import Translator
from Admin import Admin


class User_Factory(UserTyp):
    @staticmethod
    def getUserTyp(type, name):
        if type == 'user':
            return User(name)
        if type == 'translator':
            return Translator(name)
        if type == 'admin':
            return Admin(name)