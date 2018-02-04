import json
import importlib
from Deck.card import Card
from Deck.deck import Deck
""" This encapsulates the needed input to read and create a deck -- aka a list of cards from a file """


DEFAULT_NAME = 'DefaultDeck'
DECK_FIELD_NAME = 'deck'
CARDS_FIELD_NAME = 'cards'
CARD_DEFINITION_FIELD_NAME = 'cardDefinitions'
DECK_NAME_FIELD_NAME = 'deckName'
SEED_FIELD_NAME = 'seed'
OBJECT_NAME_FIELD_NAME = 'objectName'
IMPORT_LOCATION_FIELD_NAME = 'importLoc'
TYPE_FIELD_NAME = 'type'
REPLACEMENT_FIELD_NAME = 'replacement'
NUMBER_FIELD_NAME = 'number'
DECK_OPTIONS_FIELD = 'deckOptions'


def import_card(a_definition):
    """Import a card definition from a specified import location.
    The object is expected to inherit card and implement a constructor that takes two arguments.
    A name and a json containing all the other fields it needs to define itself."""
    object_name = get_with_default(a_definition, OBJECT_NAME_FIELD_NAME, None)
    import_loc = get_with_default(a_definition, IMPORT_LOCATION_FIELD_NAME, None)
    module = importlib.import_module(import_loc)
    return object_name, getattr(module, object_name)


def build_card_definitions(json_input):
    definitions = []
    if CARD_DEFINITION_FIELD_NAME in json_input.keys():
        for a_definition in json_input[CARD_DEFINITION_FIELD_NAME]:
            definitions.append(import_card(a_definition))
    return definitions


def get_class(card_type, all_definitions):
    for a_type, a_class in all_definitions:
        if a_type == card_type:
            return a_class
    return None


def card_with_definition(card_name, a_card, all_definitions):
    card_type = get_with_default(a_card, TYPE_FIELD_NAME, None)
    card_class = get_class(card_type, all_definitions)
    card_number = get_with_default(a_card, NUMBER_FIELD_NAME, 1)
    if card_class:
        card_object = card_class(card_name, json_values=a_card, card_definitions=all_definitions)
        if isinstance(card_object, list):
            return card_object * int(card_number)
        else:
            return [card_class(card_name, json_values=a_card, card_definitions=all_definitions)] * int(card_number)
    else:
        raise ValueError("Unable to find implementation for type {0} in {1}".format(card_type, all_definitions))


def get_cards(json_input, card_definitions):
    cards = []
    if DECK_FIELD_NAME in json_input.keys():
        input_deck = json_input[DECK_FIELD_NAME]
    else:
        return cards
    if CARDS_FIELD_NAME in input_deck.keys():
        for card_name in sorted(input_deck[CARDS_FIELD_NAME].keys()):
            card_value = input_deck[CARDS_FIELD_NAME][card_name]
            if isinstance(card_value, dict):
                cards.extend(card_with_definition(card_name, card_value, card_definitions))
            else:
                cards.extend([Card(card_name)]*int(card_value))
    return cards


def build_cards(json_input):
    card_definitions = build_card_definitions(json_input)
    cards = get_cards(json_input, card_definitions)
    return cards


def get_with_default(json_input, param, default_value, exception_if_fail=True):
    if param in json_input:
        return json_input[param]
    elif default_value is not None:
        return default_value
    elif exception_if_fail:
        raise ValueError("Unable to find specified field ({0}) in: {1}".format(param, json_input))
    else:
        return


def read_file(filename, override_seed=None):
    with open(filename, 'r') as in_file:
        raw = json.load(in_file)
    cards = build_cards(raw)
    name = get_with_default(raw, DECK_NAME_FIELD_NAME, DEFAULT_NAME)
    seed = get_with_default(raw, SEED_FIELD_NAME, override_seed, exception_if_fail=False)
    deck_options = raw.get(DECK_OPTIONS_FIELD, {})
    deck = Deck(name=name, seed=seed)
    for key, value in deck_options.items():
        setattr(deck, key, value)
    for a_card in cards:
        deck.add_card(a_card)

    return deck

