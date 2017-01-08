
def compare_decks(deck, ref_deck):
    for test_card, expected_card in zip(deck.card_list, ref_deck.card_list):
        if not card_compare(test_card, expected_card):
            card_message(test_card, expected_card)
            assert False


def card_compare(test_card, expected_card):
    return test_card.name == expected_card.name


def card_message(card1, card2):
    print("Card %s is not the same as card %s" % (card1.name, card2.name))
