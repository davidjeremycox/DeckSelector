import random
import copy

class Deck(object):
    def __init__(self, name=None, seed=None):
        self.name = name
        self._base_list = []
        self.card_list = []
        random.seed()

    def add_card(self, card):
        self._base_list.append(card)
        self.card_list.append(card)

    def draw_cards(self, n, replacement=False):
        card_list = random.sample(self.card_list, n)
        if replacement:
            for card in card_list:
                self.remove_card(card)
        return card_list

    def draw_card(self, replacement=False):
        card = random.choice(self.card_list)
        if replacement:
            self.remove_card(card)
        return card

    def remove_card(self, card):
        index = self.card_list.index(card)
        self.card_list.remove(index)

    def reset(self):
        self.card_list = copy.deepcopy(self._base_list)
