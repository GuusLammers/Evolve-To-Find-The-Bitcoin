import pygame as pg
import os
from colors import Colors


class GenerationLabel:

    def __init__(self):
        # base generation label
        self.base_text = 'Generation: ' 
        # colors object
        self.colors = Colors()
        # color
        self.color = self.colors.white()
        # font
        pg.font.init()
        self.font = pg.font.SysFont(os.path.abspath(r'C:\Users\guusl\Documents\Guus\Coding Projects\Evolution\human-code\fonts\GemunuLibre-Medium.ttf'), 30)

    # show label on screen
    def show(self, generation, win, width):
        # create label
        label = self.font.render(self.base_text + str(generation), 1, self.color)
        # show label on screen
        win.blit(label, self.get_position(label, width))

    # get position for label
    def get_position(self, label, width):
        label_width = label.get_width()
        label_height = label.get_height()
        x = int(width/2 - label_width/2)
        y = int(width/2 - label_height/2)
        return x, y
