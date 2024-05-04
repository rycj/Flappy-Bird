import pygame as pg
from pygame.locals import *
import sys
from config import *
from Game import Game


class Menu:

    # Generuje texty v menu
    def __init__(self) -> None:
        self.colour1: tuple = White
        self.colour2: tuple = Blue
        self.colour3: tuple = Black
        self.textchange()

    def textchange(self) -> None:
        self.title: pg.Surface = titlefont.render("Flappy Bird", True, self.colour2)
        self.button1: pg.Surface = buttonfont.render("Play", True, self.colour3)
        self.button2: pg.Surface = buttonfont.render("Quit", True, self.colour3)
        self.highscorefile = open("hs.txt", "r")
        self.highscore: pg.Surface = buttonfont.render(
            self.highscorefile.read(), True, self.colour3
        )
        self.highscorefile.close()
        self.themesign: pg.Surface = themefont.render(
            "Select theme:", True, self.colour3
        )
        self.quitcover: pg.Surface = buttonfont.render("Quit", True, Gray)
        self.playcover: pg.Surface = buttonfont.render("Play", True, Gray)

    # Mění barvy hry
    def changetheme(self, theme) -> None:
        if theme == 0:
            self.colour1 = White
            self.colour2 = Blue
            self.colour3 = Black
        elif theme == 1:
            self.colour1 = Black
            self.colour2 = Green
            self.colour3 = White
        elif theme == 2:
            self.colour1 = White
            self.colour2 = Red
            self.colour3 = Black

        self.textchange()
        self.draw()

    # Kreslí menu
    def draw(self) -> None:
        screen.fill(color=self.colour1)
        pg.draw.rect(screen, self.colour2, (HW, HH - 10, SW / 5 + 40, SH / 10 + 20))
        pg.draw.rect(screen, White, (HW + 10, HH, SW / 15, SH / 10))
        pg.draw.rect(screen, Black, (HW + 20 + SW / 15, HH, SW / 15, SH / 10))
        pg.draw.rect(screen, White, (HW + 30 + 2 * SW / 15, HH, SW / 15, SH / 10))
        pg.draw.circle(screen, Blue, (HW + 10 + SW / 30, HH + SH / 20), SH / 25)
        pg.draw.circle(
            screen, Green, (HW + 10 + SW / 30 + SW / 15 + 10, HH + SH / 20), SH / 25
        )
        pg.draw.circle(
            screen, Red, (HW + 10 + SW / 30 + 2 * SW / 15 + 20, HH + SH / 20), SH / 25
        )
        screen.blit(self.button1, (bwidth, SH / 3))
        screen.blit(self.button2, (bwidth, SH * (3 / 5)))
        screen.blit(self.highscore, (bwidth, SH * 0.85))
        screen.blit(self.themesign, (HW, HH - 30 - smallfontsize / 2.35))
        screen.blit(self.title, (50, 0))
        pg.display.flip()

    # Odpovídá na input v menu
    def run(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_SPACE:
                    game = Game(self.colour1, self.colour2, self.colour3)
                    game.run()
                    return False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mpos = pg.mouse.get_pos()

                if SW / 4.35 > mpos[0] > bwidth:
                    if SH / 3 < mpos[1] < SH / 3 + smallfontsize * 1.1:
                        screen.blit(self.playcover, (bwidth, SH / 3))
                        pg.display.flip()
                        game = Game(self.colour1, self.colour2, self.colour3)
                        game.run()
                        return False
                    elif SH * (3 / 5) < mpos[1] < SH * (3 / 5) + smallfontsize * 1.1:
                        screen.blit(self.quitcover, (bwidth, SH * (3 / 5)))
                        pg.display.flip()
                        sys.exit()
                elif HH - 10 < mpos[1] < HH + 10 + SH / 10:
                    if HW + 10 < mpos[0] < HW + 10 + SW / 15:
                        self.changetheme(0)
                    elif HW + 20 + SW / 15 < mpos[0] < HW + 20 + 2 * SW / 15:
                        self.changetheme(1)
                    elif HW + 30 + 2 * SW / 15 < mpos[0] < HW + 30 + 3 * SW / 15:
                        self.changetheme(2)
