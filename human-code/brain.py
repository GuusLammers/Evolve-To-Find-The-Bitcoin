import random
import math
import pygame as pg

class Brain:

    def __init__(self, size):
        # list of random Vector2s
        self.directions = [self.random() for i in range(size)]
        # tracking variable
        self.step = 0

    # return Vector2 from random angle
    def random(self):
        # random angle between 0 and 2pi
        angle = random.uniform(0, 2 * math.pi)
        # return Vector2 from angle
        return pg.Vector2(math.cos(angle), math.sin(angle))

    def mutate(self):
        # mutation rate
        mutation_rate = 0.04
        # iterate through directions
        for i in range(len(self.directions)):
            # get a random number between 0-1
            rand = random.uniform(0, 1)
            # check if random is less than mutation_rate
            if rand < mutation_rate:
                # overwrite direction
                self.directions[i] = self.random()    