import json
import random
import string


class User():
    def __init__(self, user):
        self.firstName = user["firstName"]
        self.lastName = user["lastName"]
        self.user_id = getRandomAlphaNumericString()

    def MakeAUserDictionary(self):
        dictionary = json.dumps(self.__dict__)
        return dictionary


def getRandomAlphaNumericString(stringLength=4):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


def GetUser():
    return list_user


list_user = {}


def addNewUser(user):
    newUser = User(user)
    user_add = json.loads(newUser.MakeAUserDictionary())
    list_user[user_add['user_id']] = user_add
