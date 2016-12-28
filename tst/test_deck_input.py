from Deck import deck_input
from Deck.card import Card


def test_read_file():
    test_filepath = 'Inputs/test_deck_definition.json'
    test_output = deck_input.read_file(test_filepath)
    expected_out = [Card('card1')*10, Card('card2')*5]
    assert(test_output == expected_out)