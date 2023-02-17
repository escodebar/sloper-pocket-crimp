from sloper_pocket_crimp import ComputerPlayer
from sloper_pocket_crimp import Gestures
import pytest


@pytest.fixture
def computer():
    return ComputerPlayer()


def test_computer_player_choses_a_gesture(computer):
    assert computer.choice() in Gestures
