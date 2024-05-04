from config import *


class Score:

    # Nastaví nulu a počítadlo
    def __init__(self, colour):
        self.value = 0
        self.colour = colour
        self.scorecounter = buttonfont.render(f"{self.value}", True, self.colour)

    # Navýší skóre o 1
    def update(self):
        self.value += 1
        self.scorecounter = buttonfont.render(f"{self.value}", True, self.colour)
