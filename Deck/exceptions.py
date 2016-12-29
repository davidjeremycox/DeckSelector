'''Class to hold custom exceptions for deck selector'''
class DeckSizeException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
