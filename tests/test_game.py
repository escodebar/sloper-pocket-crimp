from sloper_pocket_crimp import game
from sloper_pocket_crimp import Gestures
from sloper_pocket_crimp import Outcomes
import pytest


@pytest.mark.parametrize(
    "gesture_player_one, gesture_player_two, expected_outcome",
    [
        (Gestures.SLOPER, Gestures.SLOPER, Outcomes.DRAW),
        (Gestures.SLOPER, Gestures.POCKET, Outcomes.PLAYER_TWO_WINS),
        (Gestures.SLOPER, Gestures.CRIMP, Outcomes.PLAYER_ONE_WINS),
        (Gestures.POCKET, Gestures.SLOPER, Outcomes.PLAYER_ONE_WINS),
        (Gestures.POCKET, Gestures.POCKET, Outcomes.DRAW),
        (Gestures.POCKET, Gestures.CRIMP, Outcomes.PLAYER_TWO_WINS),
        (Gestures.CRIMP, Gestures.SLOPER, Outcomes.PLAYER_TWO_WINS),
        (Gestures.CRIMP, Gestures.POCKET, Outcomes.PLAYER_ONE_WINS),
        (Gestures.CRIMP, Gestures.CRIMP, Outcomes.DRAW),
    ],
)
def test_game_outcomes(gesture_player_one, gesture_player_two, expected_outcome):
    assert expected_outcome == game(
        gesture_one=gesture_player_one, gesture_two=gesture_player_two
    )
