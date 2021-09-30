import pygame as pg
from colors import Colors
from game_manager import GameManager

# window dimesions
WIDTH = 750

# set display caption, width, and height
win = pg.display.set_mode((WIDTH, WIDTH))
pg.display.set_caption('Human Evolution')

# colors object
colors = Colors()

# main function
def main():
    # create game manger object
    gm = GameManager(WIDTH)
    gm.update_current_level(win)
    # update display
    pg.display.update()
    # create clock object
    clock = pg.time.Clock()
    # use clock to set frame rate
    clock.tick(60)  
    # runs main loop until set to False
    run = True
    # control to check when simulation is running
    start = False
    # main loop
    while run:
        # iterate through all events
        for event in pg.event.get():
            # quit event
            if event.type == pg.QUIT:
                run = False
            # if simulation hasn't started
            if not start:
                if event.type == pg.KEYDOWN:
                    # switch to level 1
                    if event.key == pg.K_1:
                        gm.change_to_level1()
                        gm.update_current_level(win)
                        # update display
                        pg.display.update()
                    # switch to level 2
                    if event.key == pg.K_2:
                        gm.change_to_level2()
                        gm.update_current_level(win)
                        # update display
                        pg.display.update()
                    # switch to level 3
                    if event.key == pg.K_3:
                        gm.change_to_level3()
                        gm.update_current_level(win)
                        # update display
                        pg.display.update()
                    # if space is pressed start the simulation
                    if event.key == pg.K_SPACE:
                        start = True
            # if simulation is running
            else:        
                if event.type == pg.KEYDOWN:        
                    # if space is pressed end the simulation
                    if event.key == pg.K_SPACE:
                        start = False

        # if simulation has been started    
        if start:
            # update level through game_manager
            gm.update_current_level(win)
            # update display
            pg.display.update()

    # quit pygame		
    pg.quit()	    


# main function call
main()  