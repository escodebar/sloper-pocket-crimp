from sloper_pocket_crimp import exceptions
from sloper_pocket_crimp.gestures import Gestures
from sloper_pocket_crimp.outcomes import Outcomes


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

    def _list_game_modes(self, game_modes):
        print("Choose a game mode from the following list:")
        print(
            "\n".join(
                f"{index}: {game_mode.name.replace('_', ' ').title()}"
                for index, game_mode in enumerate(game_modes)
            )
        )

    def outcome(self, gesture_one, gesture_two):
        try:
            return self._rules_lookup_table[(gesture_one, gesture_two)]
        except KeyError:
            raise exceptions.InvalidGesture
