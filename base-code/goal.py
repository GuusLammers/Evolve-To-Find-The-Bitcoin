import pygame as pg
from colors import Colors


class Goal:

    def __init__(self, pos):
        # goals position
        self.pos = pg.Vector2(pos)
        # colors object
        self.colors = Colors()
        # goal color
        self.color = self.colors.red()
        # goal radius
        self.radius = 6

    # show goal
    def show(self, win):
        pg.draw.circle(win, self.color, (self.pos.x, self.pos.y), self.radius)     