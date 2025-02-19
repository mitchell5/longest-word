from src.longest_word.game import Game
class TestGame:

    def test_game_initialization(self):
        game = Game()
        assert isinstance(game.grid, list)
        assert len(game.grid) == 9
        assert all(char.isalpha() for char in game.grid)

    def test_empty_word_is_invalid(self):
        # empty word is not valid for the game
        game = Game()
        assert game.is_valid("") is False

    def test_word_is_valid(self):
        game = Game()
        test_grid = "KWEUEAKRZ"
        test_word = "EUREKA"
        game.grid = list(test_grid)
        assert game.is_valid(test_word) is True
        assert game.grid == list(test_grid)     # make sure the grid is the same

    def test_word_is_invalid(self):
        game = Game()
        test_grid = "KWEUEAKRZ"
        test_word = "ATABERK"
        game.grid = list(test_grid)
        assert game.is_valid(test_word) is False
        assert game.grid == list(test_grid)  # make sure that game grid is the same
