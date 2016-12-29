from Deck.deck import Deck
from Deck.card import Card
from Deck.exceptions import DeckSizeException

def build_sample_deck():
    names = ['First Card', 'Second Card', 'Third Card']
    cards = [Card(name) for name in names]
    return cards

def test_draw_too_many_cards():
    deck = Deck('Test Deck')
    deck.add_cards(build_sample_deck())
    try:
        deck.draw_cards(10)
    except DeckSizeException:
        pass
    except Exception as err:
        print('Unexpected exception: %s' % str(err))
        assert False

def test_draw_cards():
    deck = Deck('Test Deck', seed=10)
    deck.add_cards(build_sample_deck())
    cards = deck.draw_cards(2)
    ref_names = ['Third Card', 'First Card']
    for card, name in zip(cards, ref_names):
        if card.name != name:
            print('Unexpected card drawn: %s expected: %s' % (card.name, name))
            assert False

def test_draw_card_reshuffle():
    deck = Deck('Test Deck', seed=10)
    deck.add_cards(build_sample_deck())
    deck.reshuffle = True
    cards = deck.draw_cards(5)
    ref_names = ['Third Card', 'First Card', 'Second Card', 'Second Card', 'First Card']
    for card, name in zip(cards, ref_names):
        if card.name != name:
            print('Unexpected card drawn: %s expected: %s' % (card.name, name))
            assert False