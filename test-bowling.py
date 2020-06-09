import pytest

@pytest.fixture()
def game():
    return Game()

def play_bowling(current_score, rolls, pins):
    return 0

def test_gutter_game(game):
    result = play_bowling(current_score=0, rolls=20, pins=0)
    assert result == 0

def test_all_ones(game)
