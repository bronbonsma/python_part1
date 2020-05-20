import json
import random
import string


class Instrument:
    def __init__(self, instrument):
        self.type = instrument["type"]
        self.userId = "No user"
        self.id = randomid()
        self.video = "link"

    def MakeAInstrumentDictionary(self):
        dictionary = json.dumps(self.__dict__)
        return dictionary


def randomid(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def GetInstruments():
    return list_instruments


list_instruments = {}


def addNewInstrument(instrument):
    newInstrument = Instrument(instrument)
    instrument_add = json.loads(newInstrument.MakeAInstrumentDictionary())
    list_instruments[instrument_add['id']] = instrument_add


def add_key_to_instrument(key, value, instrument_id):
    list_instruments[instrument_id][key] = value

