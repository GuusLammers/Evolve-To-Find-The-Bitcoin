import pygame as pg
from level import Level


class GameManager:

    def __init__(self, width):
        self.pop_size = 25
        self.width = width
        self.current_level = None
        self.change_to_level1()

    def change_to_level1(self):
        self.current_level = Level(
            self.width,
            pg.Vector2(100, 100),
            pg.Vector2(self.width-175, self.width-125),
            self.pop_size,
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\background1.png",
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\foreground1.png"
        )

    def change_to_level2(self):
        self.current_level = Level(
            self.width,
            pg.Vector2(100, 100),
            pg.Vector2(self.width - 150, self.width - 100),
            self.pop_size,
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\background2.png",
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\foreground2.png"
        )

    def change_to_level3(self):
        self.current_level = Level(
            self.width,
            pg.Vector2(100 , 150),
            pg.Vector2(self.width - 140, self.width - 120),
            self.pop_size,
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\background3.png",
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\foreground3.png"
        )      

    def update_current_level(self, win):
        self.current_level.update(win)    