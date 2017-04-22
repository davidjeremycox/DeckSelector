from Deck.deck import Deck
from Deck.card import Card
from Deck.exceptions import DeckSizeException
import UnitTestHelper.helper_functions as helper

def build_sample_deck(seed=None):
    names = ['First Card', 'Second Card', 'Third Card']
    cards = [Card(name) for name in names]
    deck = Deck('Test Deck', seed=seed)
    deck.add_cards(cards)
    return deck


def test_draw_too_many_cards():
    deck = build_sample_deck()
    try:
        deck.draw_cards(10)
    except DeckSizeException:
        pass
    except Exception as err:
        print('Unexpected exception: %s' % str(err))
        assert False


def test_draw_cards():
    deck = build_sample_deck(10)
    cards = deck.draw_cards(2)
    ref_names = ['Third Card', 'First Card']
    for ind, (card, name) in enumerate(zip(cards, ref_names)):
        helper.print_if_assert('Unexpected card %s' % ind, card.name, name)


def test_draw_card_reshuffle():
    deck = build_sample_deck(10)
    deck.reshuffle = True
    cards = deck.draw_cards(5)
    ref_names = ['Third Card', 'First Card', 'Second Card', 'Second Card', 'First Card']
    for ind, pair in enumerate(zip(cards, ref_names)):
        card, name = pair
        if card.name != name:
            print('Unexpected card pos: %s drawn %s expected: %s' % (ind, card.name, name))
            assert False

def test_grab_splits_fail():
    deck = build_sample_deck(10)
    try:
        _, _ = deck.grab_splits(5, False)
    except DeckSizeException:
        pass

def test_grab_splits():
    deck = build_sample_deck(10)
    first, second = deck.grab_splits(2, False)
    ref_first, ref_second = 2, 0
    helper.print_if_assert('First split', first, ref_first)
    helper.print_if_assert('Second split', second, ref_second)
