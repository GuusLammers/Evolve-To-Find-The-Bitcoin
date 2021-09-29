import pygame as pg
from level import Level


class GameManager:

    def __init__(self, width):
        self.pop_size = 5
        self.level1 = Level(
            width,
            pg.Vector2(100, 100),
            pg.Vector2(width-175, width-125),
            self.pop_size,
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\background1.png",
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\foreground1.png"
        )
        self.level2 = Level(
            width,
            pg.Vector2(100, 100),
            pg.Vector2(200, 200),
            self.pop_size,
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\background2.png",
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\foreground2.png"
        )
        self.level3 = Level(
            width,
            pg.Vector2(100, 100),
            pg.Vector2(200, 200),
            self.pop_size,
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\background3.png",
            r"C:\Users\guusl\Documents\Guus\Coding Projects\Evolve-To-Find-The-Bitcoin\human-code\images\foreground3.png"
        )
        self.current_level = self.level1

    def change_to_level1(self):
        self.current_level = self.level1

    def change_to_level2(self):
        self.current_level = self.level2

    def change_to_level3(self):
        self.current_level = self.level3        

    def update_current_level(self, win):
        self.current_level.update(win)    