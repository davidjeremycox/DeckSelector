import random
import copy
from Deck.exceptions import DeckSizeException


class Deck(object):
    def __init__(self, name=None, seed=None):
        self.name = name
        self._base_list = []
        self.card_list = []
        self.reshuffle = False
        random.seed(seed)

    def add_cards(self, cards):
        for card in cards:
            self.add_card(card)

    def add_card(self, card):
        self._base_list.append(card)
        self.card_list.append(card)

    def draw_cards(self, n, replacement=False):
        first_grab, second_grab = self.grab_splits(n, replacement)
        card_list = random.sample(self.card_list, first_grab)
        if not replacement:
            self.remove_cards(card_list)
            if self.reshuffle and len(self.card_list) == 0:
                self.reset()
        if second_grab > 0:
            card_list.extend(self.draw_cards(second_grab, replacement))
        return card_list

    def grab_splits(self, n, replacement):
        if n > len(self.card_list) and self.reshuffle:
            first_grab = len(self.card_list)
            second_grab = n - len(self.card_list)
        elif n > len(self.card_list) and not replacement:
            raise DeckSizeException('Tried to draw too many cards, %s requested, %s left' %
                                    (n, len(self.card_list)))
        else:
            first_grab = n
            second_grab = 0
        return first_grab, second_grab

    def draw_card(self, replacement=False):
        card = random.choice(self.card_list)
        if not replacement:
            self.remove_card(card)
        return card

    def remove_card(self, card):
        self.card_list.remove(card)

    def remove_cards(self, cards):
        for card in cards:
            self.remove_card(card)

    def reset(self):
        self.card_list = copy.deepcopy(self._base_list)
