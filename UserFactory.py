from UserTyp import UserTyp
from User import User
from Translator import Translator
from Admin import Admin


class User_Factory(UserTyp):

    instance = None

    def __new__(cls, UfName):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        cls.instance.Uf = UfName
        return cls.instance

    def callName(cls):
        print(cls.instance.Uf)

    @staticmethod
    def getUserTyp(type, name):
        if type == 'user':
            return User(name)
        if type == 'translator':
            return Translator(name)
        if type == 'admin':
            return Admin(name)