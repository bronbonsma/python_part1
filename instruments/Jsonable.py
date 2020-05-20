from instruments.instrument import Instrument
import json


class JsonablePost(Instrument):
    def __init__(self, instrument):
        super().__init__(instrument)

    def json_parse(self):
        return json.dumps(self, default=lambda o: o.__dict__)