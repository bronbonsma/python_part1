from Exercises.BasePost import BasePost
import datetime


class ExtendedPost(BasePost):

    def __init__(self, post):
        super().__init__(post)
        self.createdAt = str(datetime.datetime.now())


