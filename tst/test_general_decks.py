import pickle
import Deck.deck_input as deck_input
import tst.compare_decks as compare_decks
import UnitTestHelper.filepath as filepath


def get_deck_names():
    return ['test_deck_definition', 'test_meal_definition', 'test_nested_definition']


def build_reference_decks():
    print('Rebuilding general deck references')
    for name in get_deck_names():
        print('Building reference deck for %s' % name)
        build_reference_deck(name)


def build_reference_deck(deck_name):
    filename = get_filename(deck_name)
    deck = deck_input.read_file(filename)
    reference_name = get_reference_name(deck_name)
    with open(reference_name, 'wb') as outfile:
        pickle.dump(deck, outfile)


def get_filename(deck_name):
    return filepath.localpath(deck_name + '.json', 'tst/Inputs/')


def get_reference_name(deck_name):
    return filepath.localpath(deck_name + '.pk', 'tst/References/')


def test_decks():
    for deck_name in get_deck_names():
        yield check_deck_name, deck_name


def check_deck_name(deck_name):
    filename = get_filename(deck_name)
    reference_name = get_reference_name(deck_name)
    deck = deck_input.read_file(filename)
    with open(reference_name, 'rb') as infile:
        ref_deck = pickle.load(infile)
    compare_decks.compare_decks(deck, ref_deck)

if __name__ == '__main__':
    build_reference_decks()
