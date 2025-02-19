import random
import string

def generate_random_word(length=9):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class Game:
    def __init__(self) -> list:
        """Attribute a random grid of size 9"""
        self.grid = list(generate_random_word())
        self.word = ""

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        else:
            # length of word should be less than or equal to the grid
            if len(word) > len(self.grid):
                    return False
            else:
                for ch in word:
                    # characters in a word should be in the grid
                    if ch not in self.grid:
                        return False
                    else:
                        # Count of characters in the word should be less than or equal to the character count in grid
                        if word.count(ch) <= self.grid.count(ch):
                            return True
                        else:
                            return False
