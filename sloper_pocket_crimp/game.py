from enum import Enum
from sloper_pocket_crimp import exceptions
from sloper_pocket_crimp.gestures import Gestures
from sloper_pocket_crimp.outcomes import Outcomes
from sloper_pocket_crimp.players import ComputerPlayer
from sloper_pocket_crimp.players import HumanPlayer


class GameModes(Enum):
    MACHINE_VS_MACHINE = 1
    HUMAN_VS_MACHINE = 2


class Game:
    _rules_lookup_table = {
        (Gestures.SLOPER, Gestures.SLOPER): Outcomes.DRAW,
        (Gestures.SLOPER, Gestures.POCKET): Outcomes.PLAYER_TWO_WINS,
        (Gestures.SLOPER, Gestures.CRIMP): Outcomes.PLAYER_ONE_WINS,
        (Gestures.POCKET, Gestures.SLOPER): Outcomes.PLAYER_ONE_WINS,
        (Gestures.POCKET, Gestures.POCKET): Outcomes.DRAW,
        (Gestures.POCKET, Gestures.CRIMP): Outcomes.PLAYER_TWO_WINS,
        (Gestures.CRIMP, Gestures.SLOPER): Outcomes.PLAYER_TWO_WINS,
        (Gestures.CRIMP, Gestures.POCKET): Outcomes.PLAYER_ONE_WINS,
        (Gestures.CRIMP, Gestures.CRIMP): Outcomes.DRAW,
    }

    _player_generation_lookup_table = {
        GameModes.MACHINE_VS_MACHINE: (ComputerPlayer, ComputerPlayer),
        GameModes.HUMAN_VS_MACHINE: (HumanPlayer, ComputerPlayer),
    }

    def _list_game_modes(self, game_modes):
        print("Choose a game mode from the following list:")
        print(
            "\n".join(
                f"{index}: {game_mode.name.replace('_', ' ').title()}"
                for index, game_mode in enumerate(game_modes)
            )
        )

    def _choose_game_mode(self, game_modes):
        choice = int(
            input(
                "Which game do you pick? {'/'.join(map(str, range(len(game_modes))))} :"
            )
        )
        return game_modes[choice]

    def generate_players(self, game_mode):
        return [klass() for klass in self._player_generation_lookup_table[game_mode]]

    def outcome(self, gesture_one, gesture_two):
        try:
            return self._rules_lookup_table[(gesture_one, gesture_two)]
        except KeyError:
            raise exceptions.InvalidGesture
