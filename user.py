from json import JSONEncoder

class User(JSONEncoder):

    username = ""
    password = ""

    def __init__(self):
        self

    def show_user_for_debug(self):
        print("{0}, {1}".format(self.username, self.password))

    def as_json(self):
        return self.__dict__
