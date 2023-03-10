from random import choice


class ComputerPlayer:
    def choice(self, gestures):
        return choice(gestures)


class HumanPlayer:
    def _list_available_gestures(self, gestures):
        print("Choose a gesture from the following list:")
        print(
            "\n".join(
                f"{index}: {gesture.name.title()}"
                for index, gesture in enumerate(gestures)
            )
        )

    def _chose_gesture(self, gestures):
        choice = int(
            input(
                "Which gesture do you pick? {'/'.join(map(str, range(len(gestures))))} :"
            )
        )
        return gestures[choice]

    def choice(self, gestures):
        while True:
            try:
                self._list_available_gestures(gestures)
                return self._chose_gesture(gestures)
            except (ValueError, IndexError):
                print(
                    "Oopsie! That was not a valid gesture.\n"
                    f"Please use the numbers from 0 to {len(gestures)}"
                )
            else:
                break
