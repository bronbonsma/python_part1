import json
import random
import string


class User():
    def __init__(self, user):
        self.firstName = user['FirstName']
        self.lastName = user["lastName"]
        self.User_id = getRandomAlphaNumericString()

    def MakeAUserDictionary(self):
        dictionary = json.dumps(self.__dict__)
        return dictionary


def getRandomAlphaNumericString(stringLength=4):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

