import pygame as pg
from colors import Colors
from brain import Brain

class Dot:

    def __init__(self, pos, best_dot=False):
        # initialize brain
        self.brain = Brain(250)
        # spawn point
        self.pos = pg.Vector2(pos)
        # starting velocity
        self.vel = pg.Vector2(0,0)
        # starting acceleration
        self.acc = pg.Vector2(0,0)
        # colors object
        self.colors = Colors()
        # dot color
        self.color = self.colors.white()
        # dot radius
        self.radius = 4
        # is the dot dead
        self.dead = False
        # dot fitness
        self.fitness = 0
        # has dot rachec the goal
        self.reached_goal = False
        # is best dot
        self.is_best = best_dot
        # call is_best
        self.if_best()

    # method to kill the dot
    def kill(self):
        self.dead = True

    # if best dot change appearance
    def if_best(self):
        if self.is_best:
            self.color = self.colors.green()
            self.radius = 5    

    # method to show dot on screen
    def show(self, win):
        pg.draw.circle(win, self.color, (self.pos.x, self.pos.y), self.radius)

    # method to move dot around
    def move(self):
        # let brain set acceleration
        if len(self.brain.directions) > self.brain.step:
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step += 1
        # if dot runs out of directions kill it
        else:
            self.kill()
        # set velocity
        self.vel += self.acc
        # limit velocity
        if self.vel.magnitude() > 5:
            self.vel = self.vel.normalize() * 5
        # set position
        self.pos += self.vel    

    # updates the dot every clock cycle
    def update(self, win_width, win_height, goal_pos):
        # if the dot is dead don't update it
        if not self.dead and not self.reached_goal:
            # move the dot
            self.move()   
            # check if the dot has gone off the screen
            if self.pos.x < 0 or self.pos.x > win_width - 5 or self.pos.y < 0 or self.pos.y > win_height - 5: 
                # kill the dot
                self.kill()
            # if goal has been reached   
            if self.pos.distance_to(goal_pos) < 5:
                # set goal reached to true
                self.reached_goal = True 
  
    # calculate fitness
    def calculate_fitness(self, goal_pos):
        # check if dot reached goal
        if self.reached_goal:
            # fitness will be calculated by taking the inverse of the steps taken divided by 100
            self.fitness = 1 / ((self.brain.step / 100) ** 2)
        else:    
            # fitness will be calculated by taking the inverse of the distance to the goal squared
            self.fitness = 1 / (self.pos.distance_to(goal_pos) ** 2)

    # clone brain from parent
    def clone(self, parent):
        # set brain equal to parents brain
        self.brain.directions = parent.brain.directions.copy()
