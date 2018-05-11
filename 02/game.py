#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import itertools
import random

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def draw_letters():
    """Return NUM_LETTERS letters randomly selected from POUCH"""
    return random.sample(POUCH, NUM_LETTERS)

def get_possible_dict_words(letters):
    """Return list of words from DICTIONARY that can be made from letters"""
    return [x for x in _get_permutations_draw(letters) if x in DICTIONARY]

def _get_permutations_draw(letters):
    perms =  [list(itertools.permutations(letters, n)) for n in range(1, NUM_LETTERS + 1)]
    return set([''.join(x) for perm in perms for x in perm])

def _validate(guess, draw):
    """Ensure that all letters of guess are in draw, and guess is in DICTIONARY"""
    pass

def calc_score(player_score, optimal_score):
    pass

def main():
    pass


if __name__ == "__main__":
    main()

print(get_possible_dict_words('apple'))