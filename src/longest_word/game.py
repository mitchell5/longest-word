"""
    The module contains the longest word game class and its methods.

    Author: S.Deniz Özkaymak
    Date: 2025-02-19
"""

import random
import string

class Game:
    """
        A class representing a word game.

        Attributes:
            grid (list): List of character grid for the game.
                         Length is 9.
    """

    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = list(self.generate_random_word())

    def generate_random_word(self, length=9):
        """ Generates random, uppercased word having length of 9
            Parameters:
            length (int) : default 9, defines the length of word.

            Returns:
            string: 9 lettered random word
        """
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def is_valid(self, word: str) -> bool:
        """ Return True if and only if the word is valid, given the Game's grid
            Parameters:
            word (str): takes a string

            Returns:
            boolean: True or False
        """
        if not word:
            return False

        # length of word should be less than or equal to the grid
        if len(word) > len(self.grid):
            return False

        # characters in a word should be in the grid
        for ch in word:
            if ch not in self.grid:
                return False

            # Count of characters in the word should be less than or
            # equal to the character count in grid
            if word.count(ch) > self.grid.count(ch):
                return False

        return True
