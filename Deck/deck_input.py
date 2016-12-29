import json
from card import Card
from Deck.deck import Deck
""" This encapsulates the needed input to read and create a deck -- aka a list of cards from a file """


DEFAULT_NAME = 'DefaultDeck'


def build_card(a_definition):
    pass


def build_card_definitions(json_input):
    definitions = []
    if 'card_definitions' in json_input.keys():
        for a_definition in json_input['card_definitions']:
            definitions.append(build_card(a_definition))
    return definitions


def card_with_definition(a_card, all_defintions):
    pass


def get_cards(json_input, card_definitions):
    cards = []
    if 'cards' in json_input.keys():
        for card_name in sorted(json_input['cards'].iterkeys()):
            card_value = json_input['cards'][card_name]
            if isinstance(card_value, dict):
                cards.append(card_with_definition(card_value, card_definitions))
            else:
                cards.extend([Card(card_name)]*int(card_value))
    return cards


def build_cards(json):
    card_definitions = build_card_definitions(json)
    cards = get_cards(json, card_definitions)
    return cards


def get_with_default(json_input, param, default_value):
    if param in json_input:
        return json_input[param]
    else:
        return default_value


def read_file(filename, override_seed=None):
    with open(filename, 'r') as in_file:
        raw = json.load(in_file)
    cards = build_cards(raw)
    name = get_with_default(raw, 'deckName', DEFAULT_NAME)
    seed = get_with_default(raw, 'seed', override_seed)
    deck = Deck(name=name, seed=seed)
    for a_card in sorted(cards):
        deck.add_card(a_card)

    return deck

