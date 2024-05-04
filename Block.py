import pygame as pg
import random
from config import *


class Block:

    # Nastaví počáteční pozici, rychlost a šířku a náhodně umístí mezeru
    def __init__(self, x: int) -> None:
        self.pos: float = bxpos + x * SW / blockcount
        self.speed: float = bspd
        self.gapheight: int = random.randint(0, SH - 220)
        self.width: float = bwidth
        self.columnhigh = pg.Rect(self.pos, 0, self.width, self.gapheight)
        self.columnlow = pg.Rect(
            self.pos, self.gapheight + 220, self.width, SH - self.gapheight - 220
        )

    # Posouvá
    def move(self) -> None:
        self.pos += self.speed

    # Přesune blok zpátky doprava a znovu náhodně umístí mezeru
    def reset(self) -> None:
        self.gapheight = random.randint(0, SH - 220)
        self.pos = bxpos
