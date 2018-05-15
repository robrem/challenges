#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
from collections import Counter
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
    return [x for x in _get_permutations_draw(letters) if x.lower() in DICTIONARY]

def _get_permutations_draw(letters):
    """Return set of all permutations of letters of length 1 through NUM_LETTERS inclusive"""
    perms =  [list(itertools.permutations(letters, n)) for n in range(1, NUM_LETTERS + 1)]
    return set([''.join(x) for perm in perms for x in perm])

def _validation(guess, draw):
    """Ensure that all letters of guess are in draw, and guess is in DICTIONARY"""
    if len(guess) > len(draw):
        return False
    if guess.lower() not in DICTIONARY:
        return False
    # Resulting Counter will be empty if guess CAN be made from draw
    return not Counter(guess) - Counter(draw)

def calc_score(player_score, optimal_score):
    return player_score / optimal_score

def main():
    draw = draw_letters()
    print(f'Letters drawn: {", ".join(draw)}')

    while True:
        guess = input('Form a valid word: ').upper()
        if not _validation(guess, draw):
            print('Invalid guess. Try again.')
        else:
            break

    guess_value = calc_word_value(guess)
    print(f'Word chosen: {guess} (value: {guess_value})')
    optimal_word = max_word_value(get_possible_dict_words(draw))
    optimal_value = calc_word_value(optimal_word)
    print(f'Optimal word possible: {optimal_word} (value: {optimal_value})')
    score = round(calc_score(guess_value, optimal_value), 1)
    print(f'You scored: {score}')

if __name__ == "__main__":
    main()