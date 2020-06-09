from bowling import play_bowling
#import pytest

#@pytest.fixture()
def test_gutter_game():
    result = play_bowling(current_score=0, rolls=20, pins=0)
    assert result == 0

#def test_all_ones(game)
