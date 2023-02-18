from sloper_pocket_crimp import ComputerPlayer
from sloper_pocket_crimp import HumanPlayer
from sloper_pocket_crimp import Gestures
from unittest.mock import MagicMock
import pytest


@pytest.fixture
def gestures():
    return list(Gestures)


@pytest.fixture
def computer():
    return ComputerPlayer()


def test_computer_player_choses_a_gesture(computer, gestures):
    assert computer.choice(gestures) in Gestures


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
def test_human_player_chose_gesture(monkeypatch, human, chosen_value, gestures):
    monkeypatch.setattr("builtins.input", lambda _: str(chosen_value))

    assert gestures[chosen_value] == human._chose_gesture(gestures)


@pytest.mark.parametrize(
    "chosen_values, expected_gesture",
    [
        ((-10, 0), Gestures.SLOPER),
        (("x", "y", 1), Gestures.POCKET),
        ((None, True, False, 2), Gestures.CRIMP),
    ],
)
def test_human_is_repeteadly_asked_for_input_given_invalid_input(
    monkeypatch,
    human,
    gestures,
    chosen_values,
    expected_gesture,
):
    list_available_gestures_mock = MagicMock()
    monkeypatch.setattr(human, "_list_available_gestures", list_available_gestures_mock)

    inputs = iter(chosen_values)
    monkeypatch.setattr("builtins.input", lambda _: str(next(inputs)))

    chosen_gesture = human.choice(gestures)

    assert len(chosen_values) == len(list_available_gestures_mock.mock_calls)
    assert expected_gesture == chosen_gesture
