import random
import string

def generate_random_word(length=9):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = list(generate_random_word())

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        pass # TODO
