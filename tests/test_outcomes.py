import pytest
from sloper_pocket_crimp import Outcomes


@pytest.mark.parametrize("outcome", ["PLAYER_ONE_WINS", "DRAW", "PLAYER_TWO_WINS"])
def test_gesture_exist(outcome):
    assert getattr(Outcomes, outcome, False)
