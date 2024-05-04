import pygame as pg
from pygame.locals import *
import time
import sys
from config import *
from Block import Block
from Score import Score
from Bird import Bird


class Game:

    # Vytváří objekty
    def __init__(self, colour1: tuple, colour2: tuple, colour3: tuple) -> None:
        self.colour1 = colour1
        self.colour2 = colour2
        self.colour3 = colour3
        self.score = Score(self.colour3)
        self.bird = Bird(self.colour2)
        self.blocks: list[Block] = []

        for i in range(blockcount):
            self.blocks.append(Block(i))

        self.abn: int = 0
        self.activeblock: Block = self.blocks[self.abn]

        if self.abn == 0:
            self.lastblock: Block = self.blocks[len(self.blocks) - 1]
        else:
            self.lastblock: Block = self.blocks[self.abn - 1]
        self.play: bool = True

    def updatehs(self) -> None:
        highscore = int(open("hs.txt", "r").read())
        if int(self.score.value) > highscore:
            highscore_file = open("hs.txt", "w")
            highscore_file.write(str(self.score.value))
            highscore_file.close()

    # Kontroluje input a reaguje na něj
    def input(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.play = False
                sys.exit()

            # Esc vrací do menu (ale ukládá highscore (viz fce."die"))
            elif event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    for block in self.blocks:
                        if block.pos <= self.bird.place:
                            self.score.value += 1
                        self.updatehs()
                    self.play = False
                elif event.key == K_SPACE:
                    self.bird.flap()

    # Obnoví grafiku hry
    def draw(self) -> None:
        screen.fill(color=self.colour1)

        for block in self.blocks:
            pg.draw.rect(screen, self.colour2, block.columnlow)
            pg.draw.rect(screen, self.colour2, block.columnhigh)

        self.bird.draw()
        screen.blit(self.score.scorecounter, (50, 20))
        pg.display.flip()

    # Nastaví highskóre a vypne play -> pošle hráče do menu
    def die(self) -> None:
        self.updatehs()
        self.play = False
        del self

    # Kontroluje zda pozice dvou mezer nejsou příliš vzdálené
    def impossiblecheck(self) -> bool:
        if -(basespeed * (3 / 4)) / abs(self.activeblock.speed) < (
            (abs(self.activeblock.gapheight - self.lastblock.gapheight))
            / (SW / blockcount - self.activeblock.width)
        ):
            return True
        else:
            return False

    # Za určitých podmínek zvýší obtížnost hry
    def speedup(self) -> None:
        if int(self.score.value) % 5 == 0:
            if self.blocks[0].speed > -basespeed:
                for block in self.blocks:
                    block.speed *= 1.3

    # Zjišťuje zda hráč nenaboural
    def checkcrash(self) -> bool:
        if self.bird.collision.colliderect(self.activeblock.columnlow):
            return True
        elif self.bird.collision.colliderect(self.activeblock.columnhigh):
            return True
        elif self.bird.pos >= SH:
            # Skóre se zvyšuje až při resetu dané překážky, pokud hráč proletí a vzápětí spadne, nepřijde o svůj bod
            for block in self.blocks:
                if block.pos <= self.bird.place:
                    self.score.update()
            return True
        return False

    # Aplikuje gravitační zrychlení
    def gravity(self) -> None:
        self.bird.speed += speedchange

    # Obnoví stav hry
    def update(self) -> None:

        # Vše se posune
        self.gravity()
        self.bird.move()

        for block in self.blocks:
            block.move()

        # Reset bloků na konci, update skóre a kontrola proveditelnosti
        if self.activeblock.pos <= -self.activeblock.width:
            self.speedup()
            self.score.update()
            self.activeblock.reset()

            while self.impossiblecheck == True:
                self.activeblock.reset()

            if self.abn == len(self.blocks) - 1:
                self.abn = 0
            else:
                self.abn += 1

            self.activeblock = self.blocks[self.abn]

            if self.abn == 0:
                self.lastblock = self.blocks[len(self.blocks) - 1]
            else:
                self.lastblock = self.blocks[self.abn - 1]

        self.bird.collision.y = self.bird.pos - 25

        for block in self.blocks:
            block.columnhigh.x = block.pos
            block.columnlow.x = block.pos

        # Kontrola smrti
        if self.checkcrash():
            self.die()

    def run(self) -> None:
        while self.play:
            time.sleep(0.02)
            self.input()
            self.update()
            self.draw()
