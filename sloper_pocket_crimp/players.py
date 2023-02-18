from sloper_pocket_crimp import Gestures
from random import choice


gestures = list(Gestures)


class ComputerPlayer:
    def choice(self):
        return choice(list(Gestures))


class HumanPlayer:
    def _list_available_gestures(self, gestures):
        print("Choose a gesture from the following list:")
        print(
            "\n".join(f"{index}: {gesture}" for index, gesture in enumerate(gestures))
        )

    def _chose_gesture(self, gestures):
        choice = int(
            input(
                "Which gesture do you pick? {'/'.join(map(str, range(len(gestures))))} :"
            )
        )
        return gestures[choice]

    def choice(self):
        self._list_available_gestures(gestures)
        return self._chose_gesture(gestures)
