import json
from card import Card
""" This encapsulates the needed input to read and create a deck -- aka a list of cards from a file """


def build_card(a_definition):
    pass


def build_card_definitions(json):
    definitions = []
    if 'card_definitions' in json.keys():
        for a_definition in json['card_definitions']:
            definitions.append(build_card(a_definition))
    return definitions


def get_cards(json, card_definitions):
    pass


def build_cards(json):
    card_definitions = build_card_definitions(json)
    cards = get_cards(json, card_definitions)
    return cards


def read_file(filename):
    output_list = []
    with open()
    raw = json.loads(filename)
    output_list.extend(build_cards(raw))

    return output_list

