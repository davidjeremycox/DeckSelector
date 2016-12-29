from optparse import OptionParser

import Deck.deck_input as deck_input

def _setup_and_parse_args():
    usage = ("%prog [options] [args]\n"
             "\tCreate a deck and draw one or more cards from it")
    opt = OptionParser(usage=usage)
    opt.add_option('-d', '--deck', dest='deck_file', help='File to create deck from')
    opt.add_option('-n', '--number', dest='draws', help='Number of cards to draw (defaults to 1)',
                   default=1)
    opt.add_option('-r', '--replacement', dest='replacement', action='store_true',
                   help='Draw with replacement (defaults to false)')
    return opt.parse_args()

if __name__ == '__main__':
    options, args = _setup_and_parse_args()

    deck = deck_input.read_file(options.deck_file)
    cards = deck.draw_cards(options.draws, options.replacement)
    for card in cards:
        print(card.name)
