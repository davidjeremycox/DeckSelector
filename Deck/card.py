
class Card(object):

    def __str__(self):
        return self.name

    def __init__(self, in_name, json_values=None, card_definitions=None):
        """For compatibility any implementation should accept json_values and all_definitions as keyword arguments
        to its constructor."""
        self.name = in_name
