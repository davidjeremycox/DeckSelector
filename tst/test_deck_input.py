from Deck.card import Card
from Deck.nested_card import NestedCard
from Deck.deck import Deck
import Deck.deck_input as deck_input


def card_compare(test_card, expected_card):
    return test_card.name == expected_card.name


def card_message(card1, card2):
    print("Card %s is not the same as card %s" % (card1.name, card2.name))


def check_cards(test, expected):
    for test_card, expected_card in zip(test.card_list, expected.card_list):
        if not card_compare(test_card, expected_card):
            card_message(test_card, expected_card)
            assert False


def test_read_file():
    test_filepath = 'tst/Inputs/test_deck_definition.json'
    test_output = deck_input.read_file(test_filepath)
    expected_cards = [Card(u'card1')]*10
    expected_cards.extend([Card(u'card2')]*5)
    deck = Deck(name=deck_input.DEFAULT_NAME, seed=None)
    deck.add_cards(expected_cards)
    for test_card, expected_card in zip(test_output.card_list, deck.card_list):
        if not card_compare(test_card, expected_card):
            card_message(test_card, expected_card)
            assert False


def test_read_nested_file():
    test_filepath = 'tst/Inputs/test_nested_definition.json'
    test_output = deck_input.read_file(test_filepath)
    nested_deck = Deck(name=deck_input.DEFAULT_NAME, seed=None)
    nested_cards = [Card(u'card1a')]*5
    nested_cards.extend([Card(u'card1b')]*10)
    nested_deck.add_cards(nested_cards)
    expected_cards = []
    expected_cards.extend([NestedCard('card1', deck=nested_deck, replace_draws=False)]*3)
    expected_cards.extend([Card(u'card2')]*3)
    deck = Deck(name=deck_input.DEFAULT_NAME, seed=None)
    deck.add_cards(expected_cards)
    test_length = len(test_output.card_list)
    expected_length = len(deck.card_list)
    if not test_length == expected_length:
        print("Test Card list length %d is not the same as expected card list %d" % (test_length, expected_length))
    assert(len(test_output.card_list) == len(deck.card_list))
    check_cards(test_output, deck)


def test_factory_method():
    test_filepath = 'tst/Inputs/test_factory_definition.json'
    test_output = deck_input.read_file(test_filepath)
    cards = [Card(u'card1')]*2
    cards.extend([Card(u'card2')]*3)
    deck = Deck(name=deck_input.DEFAULT_NAME, seed=None)
    deck.add_cards(cards)
    test_length = len(test_output.card_list)
    expected_length = len(deck.card_list)
    if not test_length == expected_length:
        print("Test Card list length %d is not the same as expected card list %d" % (test_length, expected_length))
    assert(test_length == expected_length)
    check_cards(test_output, deck)

