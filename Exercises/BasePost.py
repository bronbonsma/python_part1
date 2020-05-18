
class BasePost:
    def __init__(self, post):
        self.userId = post["userId"]
        self.id = post["id"]
        self.title = post["title"]
        self.body = post["body"]
