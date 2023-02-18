from sloper_pocket_crimp import ComputerPlayer
from sloper_pocket_crimp import HumanPlayer
from sloper_pocket_crimp import Gestures
import pytest


@pytest.fixture
def computer():
    return ComputerPlayer()


def test_computer_player_choses_a_gesture(computer):
    assert computer.choice() in Gestures


@pytest.fixture
def human():
    return HumanPlayer()


@pytest.mark.xfail
@pytest.mark.parametrize("input_value", ["0", "1", "2"])
def test_human_player_choses_a_gesture(monkeypatch, human, input_value):
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    assert human.choice() in Gestures
