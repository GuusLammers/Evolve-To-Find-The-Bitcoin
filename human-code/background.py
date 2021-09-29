import pygame as pg
import os


class Background:

    def __init__(self, width, bg, fg):
        self.bg = pg.transform.scale(pg.image.load(os.path.abspath(bg)), (width, width))
        self.fg = pg.transform.scale(pg.image.load(os.path.abspath(fg)), (width, width))

    # show background
    def show(self, win):
        # show background on screen
        win.blit(self.bg, (0, 0))
        # show foreground on screen
        win.blit(self.fg, (0, 0))

    # get image mask of foreground
    def get_image_mask(self):
        return pg.mask.from_surface(self.fg)
  