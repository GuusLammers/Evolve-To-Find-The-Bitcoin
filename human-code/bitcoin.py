import pygame as pg
import os


class Bitcoin:

    def __init__(self, pos):
        # load in image
        self.image = self.stand = pg.image.load(os.path.abspath(r'C:\Users\guusl\Documents\Guus\Coding Projects\Evolution\human-code\images\bitcoin.png'))
        # scale factor
        self.scale = 15
        # scaled image
        self.image_scaled = pg.transform.scale(self.stand, (int(self.stand.get_width()/self.scale), int(self.stand.get_height()/self.scale)))
        # goals position
        self.pos = pg.Vector2(pos)

    # show bitcoin
    def show(self, win):
        # show bitcoin on screen
        win.blit(self.image_scaled, self.pos)   

    # get image mask of bitcoin
    def get_image_mask(self):
        return pg.mask.from_surface(self.image)    

