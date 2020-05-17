from Exercises.BasePost import BasePost
import datetime
import json


class ExtendedPost(BasePost):

    def __init__(self, post):
        super().__init__(post)
        self.createdAt = str(datetime.datetime.now())


class JsonablePost(ExtendedPost):
    def __init__(self, post):
        super().__init__(post)

    def json_parse(self):
        dictionary = json.dumps(self.__dict__)
        return dictionary
