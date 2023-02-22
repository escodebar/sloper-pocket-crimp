from enum import Enum
from sloper_pocket_crimp import exceptions
from sloper_pocket_crimp import ComputerPlayer
from sloper_pocket_crimp import Game
from sloper_pocket_crimp import GameModes
from sloper_pocket_crimp import Gestures
from sloper_pocket_crimp import HumanPlayer
from sloper_pocket_crimp import Outcomes
from unittest.mock import MagicMock
import pytest


@pytest.fixture
def game():
    return Game()


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
def test_game_outcome(game, gesture_player_one, gesture_player_two, expected_outcome):
    assert expected_outcome == game.outcome(
        gesture_one=gesture_player_one, gesture_two=gesture_player_two
    )


@pytest.fixture(params=[Gestures.SLOPER, Gestures.POCKET, Gestures.CRIMP])
def valid_gesture(request):
    return request.param


@pytest.fixture(params=[MagicMock(), None, 1, Outcomes.DRAW, "PAPER"])
def invalid_gesture(request):
    return request.param


def test_outcome_raises_InvalidGesture(game, valid_gesture, invalid_gesture):
    with pytest.raises(exceptions.InvalidGesture):
        game.outcome(gesture_one=valid_gesture, gesture_two=invalid_gesture)


@pytest.mark.parametrize(
    "game_modes, expected_print",
    [
        (
            Enum("GameModes", ["MACHINE_VS_MACHINE", "HUMAN_VS_MACHINE"]),
            "Choose a game mode from the following list:\n"
            "0: Machine Vs Machine\n"
            "1: Human Vs Machine\n",
        ),
        (
            Enum("GameModes", ["MACHINE_VS_MACHINE"]),
            "Choose a game mode from the following list:\n" "0: Machine Vs Machine\n",
        ),
    ],
)
def test_lists_game_modes(game, game_modes, expected_print, capsys):
    game._list_game_modes(list(game_modes))

    captured = capsys.readouterr()

    assert expected_print == captured.out


@pytest.mark.parametrize(
    "game_modes, choice",
    [
        (Enum("GameModes", ["MACHINE_VS_MACHINE", "HUMAN_VS_MACHINE"]), 1),
        (Enum("GameModes", ["MACHINE_VS_MACHINE"]), 0),
    ],
)
def test_choose_mode_selects_expected_mode(
    monkeypatch, game, game_modes, choice, capsys
):
    monkeypatch.setattr("builtins.input", lambda _: str(choice))

    game_mode_list = list(game_modes)

    chosen_mode = game._choose_game_mode(game_mode_list)

    assert game_mode_list[choice] == chosen_mode


@pytest.mark.parametrize(
    "mode, expected_player_types",
    [
        ("HUMAN_VS_MACHINE", [HumanPlayer, ComputerPlayer]),
        ("MACHINE_VS_MACHINE", [ComputerPlayer, ComputerPlayer]),
    ],
)
def test_generate_players(game, mode, expected_player_types):
    players = game.generate_players(getattr(GameModes, mode))

    player_types = list(map(type, players))

    assert expected_player_types == player_types
