import json
import random
import string


class Instrument:
    def __init__(self, instrument):
        self.type = instrument["type"]
        self.userId = instrument["userId"]
        self.instrument_id = randomid()
        self.video = instrument["link"]

    def MakeAInstrumentDictionary(self):
        dictionary = json.dumps(self.__dict__)
        return dictionary



def randomid(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

