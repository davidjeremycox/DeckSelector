from Deck.card import Card
from Deck.deck import Deck
import Deck.deck_input as deck_input


def test_read_file():
    test_filepath = 'tst/Inputs/test_deck_definition.json'
    test_output = deck_input.read_file(test_filepath)
    expected_cards = [Card(u'card1')]*10
    expected_cards.extend([Card(u'card2')]*5)
    deck = Deck(name=deck_input.DEFAULT_NAME, seed=None)
    for a_card in sorted(expected_cards):
        deck.add_card(a_card)
    for test_card, expected_card in zip(test_output.card_list, deck.card_list):
        assert(test_card == expected_card)
