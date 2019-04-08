import pytest

@pytest.fixture()
def game():
    return Game()

def test_gutter_game(game):
    assert game.get_score() == 0