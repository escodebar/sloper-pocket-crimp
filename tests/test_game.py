from sloper_pocket_crimp import exceptions
from sloper_pocket_crimp import game
from sloper_pocket_crimp import Gestures
from sloper_pocket_crimp import Outcomes
from unittest.mock import MagicMock
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


@pytest.fixture(params=[Gestures.SLOPER, Gestures.POCKET, Gestures.CRIMP])
def valid_gesture(request):
    return request.param


@pytest.fixture(params=[MagicMock(), None, 1, Outcomes.DRAW, "PAPER"])
def invalid_gesture(request):
    return request.param


@pytest.mark.xfail
def test_game_raises_InvalidGesture(valid_gesture, invalid_gesture):
    with pytest.raises(exceptions.InvalidGesture):
        game(gesture_one=valid_gesture, gesture_two=invalid_gesture)
