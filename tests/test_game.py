from src.longest_word.game import Game
class TestGame:
    def test_game_initialization(self):
            game = Game()
            assert isinstance(game.grid, list)
            assert len(game.grid) == 9
            assert all(char.isalpha() for char in game.grid)
            # teardown
