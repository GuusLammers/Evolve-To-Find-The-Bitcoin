import pygame as pg
import os
import math
from brain import Brain
import time


class Human:

    def __init__(self, pos, best_human=False):
        # images
        self.stand = pg.image.load(os.path.abspath(r'C:\Users\guusl\Documents\Guus\Coding Projects\Evolution\human-code\images\stand.png'))
        self.walk1 = pg.image.load(os.path.abspath(r'C:\Users\guusl\Documents\Guus\Coding Projects\Evolution\human-code\images\walk1.png'))
        self.walk2 = pg.image.load(os.path.abspath(r'C:\Users\guusl\Documents\Guus\Coding Projects\Evolution\human-code\images\walk2.png'))
        self.stand_best = pg.image.load(os.path.abspath(r'C:\Users\guusl\Documents\Guus\Coding Projects\Evolution\human-code\images\stand_best.png'))
        self.walk1_best = pg.image.load(os.path.abspath(r'C:\Users\guusl\Documents\Guus\Coding Projects\Evolution\human-code\images\walk1_best.png'))
        self.walk2_best = pg.image.load(os.path.abspath(r'C:\Users\guusl\Documents\Guus\Coding Projects\Evolution\human-code\images\walk2_best.png'))
        # scale factor
        self.scale = 30
        # load images for aniamtion
        self.images = [pg.transform.scale(self.stand, (int(self.stand.get_width()/self.scale), int(self.stand.get_height()/self.scale))), 
                       pg.transform.scale(self.walk1, (int(self.walk1.get_width()/self.scale), int(self.walk1.get_height()/self.scale))), 
                       pg.transform.scale(self.stand, (int(self.stand.get_width()/self.scale), int(self.stand.get_height()/self.scale))),
                       pg.transform.scale(self.walk2, (int(self.walk2.get_width()/self.scale), int(self.walk2.get_height()/self.scale)))]
        # current image in animation
        self.current_image = 0
        # counter to indicate switch to next image
        self.next_image_counter = 0
        # instantiate brain object
        self.brain = Brain(40)
        # starting position
        self.pos = pg.Vector2(pos)
        # starting velocity
        self.vel = pg.Vector2(0, 0)
        # starting acceleration
        self.acc = pg.Vector2(0, 0)
        # is the human dead
        self.dead = False
        # has the human reached its goal
        self.reached_goal = False
        # is best human
        self.best = best_human
        # humans fitness
        self.fitness = 0
        # next step counter
        self.next_step_counter = 0
        # walked off island
        self.fell_off_island = False
        # show image or not
        self.should_show = True
        # start time
        self.start_time = time.time()
        # end time
        self.end_time = 0
        # call is_best
        self.if_best()

    # move human
    def move(self):
        # if human is alive and hasnt found goal
        if not self.dead and not self.reached_goal:
            # increment next step counter
            self.next_step_counter += 1
            # check if brain has any directions left
            if len(self.brain.directions) > self.brain.step: 
                # add next direction to acceleration                  
                self.acc = self.brain.directions[self.brain.step]
                # check if next_step_counter is 25
                if self.next_step_counter > 25:
                    # reset next_step_counter
                    self.next_step_counter = 0
                    # increment brains step counter
                    self.brain.step += 1
            # if the human runs out of directions kill it
            else:    
                # kill human
                self.kill()
            # add acceleration to velocity    
            self.vel += self.acc
            # limit velocity to 5
            if self.vel.magnitude() > 2:
                self.vel = self.vel.normalize() * 2
            # add velocity to position
            self.pos += self.vel

    # show human
    def show(self, win):
        # if human is alive and hasn't reached goal
        if not self.dead and not self.reached_goal:
            # increment next_image_counter
            self.next_image_counter += 1
            # if next_image_counter is greater then
            if self.next_image_counter > 5:
                # reset next_image_counter
                self.next_image_counter = 0
                # increment current iamge
                self.current_image += 1
                # check if current image is greater than length of images
                if self.current_image > len(self.images) - 1:
                    # reset current image back to 0
                    self.current_image = 0
        # if dead
        else:
            # if died from falling off edge
            if self.fell_off_island and self.should_show:
                # increase scale factor
                self.scale += 1
                # shrink image
                self.images[0] = pg.transform.scale(self.stand, (int(self.stand.get_width()/self.scale), int(self.stand.get_height()/self.scale)))
                # if shrink factor is grester than 60
                if self.scale > 90:
                    self.should_show = False
        # if the human should be shown
        if self.should_show:
            # rotate image and show it on screen
            self.rotate_img_and_get_center(win)    

    # update human
    def update(self, win, width, island_mask, bitcoin):
        # move human
        self.move()
        # show human
        self.show(win)
        # if human is alive
        if not self.dead:
            # check if human has gone off island
            if not self.is_on_island(island_mask):
                # set fell_off_island flag
                self.fell_off_island = True
                # kill human
                self.kill()
            # check if human found the bitcoin
            elif self.found_bitcoin(bitcoin) and not self.reached_goal:
                # set end time
                self.end_time = time.time()
                # set reached_goals to True
                self.reached_goal = True 
                # set image counter to zero
                self.next_image_counter = 0
                # set current image to next_image_counter
                self.current_image = self.next_image_counter   


    # get center of image
    def rotate_img_and_get_center(self, win):
        rotated_img = pg.transform.rotate(self.images[self.current_image], self.get_direction())
        center = rotated_img.get_rect(center=self.images[self.current_image].get_rect(topleft=(self.pos.x, self.pos.y)).center)
        # show human on screen
        win.blit(rotated_img, center)

    # get direction human is traveling
    def get_direction(self):
        # if in quadrant 1
        if self.vel.x > 0 and self.vel.y > 0:
            # return angle from velocity vector in radians
            return math.degrees(math.atan(self.vel.x / self.vel.y)) + 180
        # if in quadrant 2
        elif self.vel.x < 0 and self.vel.y > 0:
            # return angle from velocity vector in radians
            return math.degrees(math.atan(self.vel.y / -self.vel.x)) + 90
        # if in quadrant 3
        elif self.vel.x < 0 and self.vel.y < 0:
            # return angle from velocity vector in radians
            return math.degrees(math.atan(-self.vel.x / -self.vel.y))
        # if in quadrant 4
        else:
            # return angle from velocity vector in radians
            return math.degrees(math.atan(-self.vel.y / self.vel.x)) + 270

    # kill human
    def kill(self):
        # set dead to True
        self.dead = True
        # set image counter to zero
        self.next_image_counter = 0
        # set current image to next_image_counter
        self.current_image = self.next_image_counter

    # get image mask of human
    def get_image_mask(self):
        return pg.mask.from_surface(self.images[self.current_image])  

    # check if human is still on island
    def is_on_island(self, island_mask):
        # determine offset
        offset = (-int(self.pos.x), -int(self.pos.y))
        # check image mask overlap
        if self.get_image_mask().overlap(island_mask, offset):
            # return True if on isalnd
            return True
        # if not on island return False
        return False    

    # check if human found bitcoin
    def found_bitcoin(self, bitcoin):
        # checks collision returns True if collision found
        if self.pos.x - bitcoin.pos.x < 15 and self.pos.y - bitcoin.pos.y < 15 and self.pos.x - bitcoin.pos.x > 0 and self.pos.y - bitcoin.pos.y > 0:
            return True
        elif self.pos.x - bitcoin.pos.x > -15 and self.pos.y - bitcoin.pos.y > -15 and self.pos.x - bitcoin.pos.x < 0 and self.pos.y - bitcoin.pos.y < 0:     
            return True
        # return false if no collision
        return False     

    # calculate fitness
    def calculate_fitness(self, goal_pos):
        # check if human found the bitcoin
        if self.reached_goal:
            # fitness will be calculated by taking the inverse of the steps taken divided by 100
            #self.fitness = 1 / ((self.brain.step / 100) ** 2)
            # fitness calculated by time required to reach goal
            self.fitness = 1 / (((self.end_time - self.start_time) / 100) ** 2)
        else:
            # fitness will be calculated by taking the inverse of the distance to the goal squared
            self.fitness = 1 / (self.pos.distance_to(goal_pos) ** 2)

    # clone brain from parent
    def clone(self, parent):
        # set brain equal to parents brain
        self.brain.directions = parent.brain.directions.copy()

    # alters dot propertise on creation if the human is the best from previous generation
    def if_best(self):
        # check if human is the best from previous generation
        if self.best:
            # replace images
            self.images = [pg.transform.scale(self.stand_best, (int(self.stand_best.get_width()/self.scale), int(self.stand_best.get_height()/self.scale))), 
                           pg.transform.scale(self.walk1_best, (int(self.walk1_best.get_width()/self.scale), int(self.walk1_best.get_height()/self.scale))), 
                           pg.transform.scale(self.stand_best, (int(self.stand_best.get_width()/self.scale), int(self.stand_best.get_height()/self.scale))),
                           pg.transform.scale(self.walk2_best, (int(self.walk2_best.get_width()/self.scale), int(self.walk2_best.get_height()/self.scale)))]

