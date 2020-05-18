import json
from Exercises.ExtendedPost import ExtendedPost


class JsonablePost(ExtendedPost):
    def __init__(self, post):
        super().__init__(post)

    def json_parse(self):
        return json.dumps(self, default=lambda o: o.__dict__)
