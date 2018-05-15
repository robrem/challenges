#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
from collections import Counter
import itertools
import random

NUM_LETTERS = 7

class SimpleScrabble:

    def __init__(self):
        self.draw = self.draw_letters()


    # re-use from challenge 01
    def calc_word_value(self, word):
        """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
        return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

    # re-use from challenge 01
    def max_word_value(self, words):
        """Calc the max value of a collection of words"""
        return max(words, key=self.calc_word_value)

    def draw_letters(self):
        """Return NUM_LETTERS letters randomly selected from POUCH"""
        return random.sample(POUCH, NUM_LETTERS)

    def get_possible_dict_words(self, letters):
        """Return list of words from DICTIONARY that can be made from letters"""
        return [x for x in self._get_permutations_draw(letters) if x.lower() in DICTIONARY]

    def _get_permutations_draw(self, letters):
        """Return set of all permutations of letters of length 1 through NUM_LETTERS inclusive"""
        perms =  [list(itertools.permutations(letters, n)) for n in range(1, NUM_LETTERS + 1)]
        return set([''.join(x) for perm in perms for x in perm])

    def _validation(self, guess, draw):
        """Ensure that all letters of guess are in draw, and guess is in DICTIONARY"""
        if len(guess) > len(draw):
            return False
        if guess.lower() not in DICTIONARY:
            return False
        # Resulting Counter will be empty if guess CAN be made from draw
        return not Counter(guess) - Counter(draw)

    def calc_score(self, player_score, optimal_score):
        return round(player_score / optimal_score, 1)

    def play(self):
        print(f'Letters drawn: {", ".join(self.draw)}')

        while True:
            guess = input('Form a valid word: ').upper()
            if not self._validation(guess, self.draw):
                print('Invalid guess. Try again.')
            else:
                break

        guess_value = self.calc_word_value(guess)
        print(f'Word chosen: {guess} (value: {guess_value})')
        optimal_word = self.max_word_value(self.get_possible_dict_words(self.draw))
        optimal_value = self.calc_word_value(optimal_word)
        print(f'Optimal word possible: {optimal_word} (value: {optimal_value})')
        score = self.calc_score(guess_value, optimal_value)
        print(f'You scored: {score}')

def main():
    game = SimpleScrabble()
    game.play()

if __name__ == "__main__":
    main()