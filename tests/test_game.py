"""
    The module contains the longest word test class.

    Author: S.Deniz Özkaymak
    Date: 2025-02-19
"""
from src.longest_word.game import Game
class TestGame:
    """ Test class for our longest word game."""

    def test_game_initialization(self):
        """  Game grid should be 9 uppercased lettered list of words. """
        game = Game()
        assert isinstance(game.grid, list)
        assert len(game.grid) == 9
        assert all(char.isalpha() for char in game.grid)

    def test_empty_word_is_invalid(self):
        """ Empty string is not a word. Thus is invalid."""
        game = Game()
        assert game.is_valid("") is False

    def test_word_is_valid(self):
        """ if a given word is in the grid, it is valid"""
        game = Game()
        test_grid = "KWEUEAKRZ"
        test_word = "EUREKA"
        game.grid = list(test_grid)
        assert game.is_valid(test_word) is True
        # make sure the grid is the same
        assert game.grid == list(test_grid)

    def test_word_is_invalid(self):
        """ if a given word is not in the grid, it should be invalid."""
        game = Game()
        test_grid = "KWEUEAKRZ"
        test_word = "ATABERK"
        game.grid = list(test_grid)
        assert game.is_valid(test_word) is False
        assert game.grid == list(test_grid)

    def test_undefined_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        game = Game()
        game.grid = list('BABYSITTER')
        assert game.is_valid("BYB") is False
