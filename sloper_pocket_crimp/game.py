from sloper_pocket_crimp.gestures import Gestures
from sloper_pocket_crimp.outcomes import Outcomes

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


def game(gesture_one, gesture_two):
    return _rules_lookup_table[(gesture_one, gesture_two)]
