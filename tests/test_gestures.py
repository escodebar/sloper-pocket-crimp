import pytest
from sloper_pocket_crimp import Gestures


@pytest.mark.xfail
@pytest.mark.parametrize("gesture", ["SLOPER", "POCKET", "CRIMP"])
def test_gesture_exist(gesture):
    assert getattr(Gestures, gesture, False)
