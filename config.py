import pygame as pg

pg.init()
pg.font.init()
info = pg.display.Info()
screen: pg.Surface = pg.display.set_mode((info.current_w, info.current_h))
pg.display.set_caption("Flappy Bird")

# Nastavení barev
Blue: tuple = (85, 173, 237)
Black: tuple = (0, 0, 0)
White: tuple = (255, 255, 255)
Gray: tuple = (112, 112, 112)
Green: tuple = (61, 255, 125)
Red: tuple = (240, 46, 78)


# Šířka a výška obrazovky (+jejich poloviny)
SW: int = info.current_w
SH: int = info.current_h
HW: float = SW / 2
HH: float = SH / 2

# Počáteční pozice, velikosti, rychlosti...
pxpos: float = SW / 5
pypos: float = HH
bxpos: int = SW
bwidth: float = SW / 15
basespeed: float = SW / 175
speedchange: float = basespeed / 20
speedlimitup: float = -basespeed / 2
pspd: float = basespeed
bspd: float = -basespeed * (2 / 3)
blockcount: int = 2


# Fonty
smallfontsize = int(SH / 8)
largefontsize = int(SH / 4)
titlefont = pg.font.Font("ptakfont.ttf", largefontsize)
buttonfont = pg.font.Font("ptakfont.ttf", smallfontsize)
themefont = pg.font.Font("ptakfont.ttf", int(smallfontsize / 2.35))

# Spuštění hudby
pg.mixer.music.load("funmusic.mp3")
pg.mixer.music.play(-1)
