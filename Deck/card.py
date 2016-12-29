
class Card(object):

    def __init__(self, in_name):
        self.name = in_name

    def __eq__(self, other):
        try:
            return self.name == other.name
        except AttributeError:
            return False

    def __lt__(self, other):
        try:
            return self.name < other.name
        except AttributeError:
            return True