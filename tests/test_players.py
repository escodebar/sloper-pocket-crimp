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


@pytest.mark.parametrize(
    "gestures, expected_print",
    [
        (
            list(Gestures),
            "Choose a gesture from the following list:\n"
            "0: Sloper\n"
            "1: Pocket\n"
            "2: Crimp\n",
        ),
        (
            list(Gestures)[:-1],
            "Choose a gesture from the following list:\n" "0: Sloper\n" "1: Pocket\n",
        ),
    ],
)
def tests_list_available_gestures(human, gestures, expected_print, capsys):
    human._list_available_gestures(gestures)

    captured = capsys.readouterr()

    assert expected_print == captured.out


@pytest.mark.parametrize("chosen_value", [0, 1, 2])
def test_human_player_chose_gesture(monkeypatch, human, chosen_value):
    monkeypatch.setattr("builtins.input", lambda _: str(chosen_value))

    gestures = list(Gestures)

    assert gestures[chosen_value] == human._chose_gesture(gestures)
