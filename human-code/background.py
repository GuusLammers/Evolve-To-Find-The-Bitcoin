import pygame as pg
import os

class Background:

    def __init__(self, width):
        self.background1 = pg.transform.scale(pg.image.load(os.path.abspath(r'C:\Users\guusl\Documents\Guus\Coding Projects\Evolution\human-code\images\background1.png')), (width, width))
        self.foreground1 = pg.transform.scale(pg.image.load(os.path.abspath(r'C:\Users\guusl\Documents\Guus\Coding Projects\Evolution\human-code\images\foreground1.png')), (width, width))

    # show background
    def show(self, win):
        # show background on screen
        win.blit(self.background1, (0, 0))
        # show foreground on screen
        win.blit(self.foreground1, (0, 0))

    # get image mask of foreground
    def get_image_mask(self):
        return pg.mask.from_surface(self.foreground1)
  