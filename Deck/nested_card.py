from Deck.card import Card
from Deck.deck import Deck
import Deck.deck_input as deck_input


class NestedCard(Card):

    def __init__(self, in_name, json_values=None, card_definitions=None, deck=None, replace_draws=None):
        super(NestedCard, self).__init__(in_name=in_name)
        self.replace_draws = replace_draws
        if (json_values is None and deck is None) or (deck is None and card_definitions is None):
            return
        if json_values is not None:
            cards = deck_input.get_cards(json_values, card_definitions)
            deck_name = deck_input.get_with_default(json_values, deck_input.DECK_NAME_FIELD_NAME, deck_input.DEFAULT_NAME)
            deck_seed = deck_input.get_with_default(json_values, deck_input.SEED_FIELD_NAME, None, False)
            deck_replacement = deck_input.get_with_default(json_values, deck_input.REPLACEMENT_FIELD_NAME, False)
            if deck_replacement == 'True':
                self.replace_draws = True
            self.deck = Deck(name=deck_name, seed=deck_seed)
            self.deck.add_cards(cards)
        elif deck is not None:
            self.deck = deck
        else:
            raise NotImplementedError("Unable to construct nested card without deck or json values")

    def __str__(self):
        if self.deck:
            card = self.deck.draw_card(self.replace_draws)
            return str(card)
        else:
            return super(NestedCard, self).__str__()
