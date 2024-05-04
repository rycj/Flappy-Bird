import pygame as pg
from config import *


class Bird:

    # Nastaví počáteční pozici a rychlost
    def __init__(self, colour: tuple) -> None:
        self.place: float = pxpos
        self.pos: float = pypos
        self.speed: float = 0.0
        self.colour: tuple = colour

        if self.colour == Blue:
            self.body = pg.image.load("ptakiconblue.png")
        elif self.colour == Green:
            self.body = pg.image.load("ptakicongreen.png")
        elif self.colour == Red:
            self.body = pg.image.load("ptakiconred.png")

        self.collision = pg.Rect(self.place - 25, self.pos - 25, 50, 50)

    # Posouvá...
    def move(self):
        self.pos += self.speed

    # Mávnutí křídly změní rychlost na basespeed směrem nahoru
    def flap(self):
        if self.speed > speedlimitup:
            self.speed = -basespeed

    # Přidá ikonu na obrazovku
    def draw(self):
        screen.blit(self.body, ((self.place) - 68, self.pos - 68))
