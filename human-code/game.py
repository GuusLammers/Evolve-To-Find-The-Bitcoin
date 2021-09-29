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

# update window
def update_win(win, game_manager):
    # update game_manager
    game_manager.update_current_level(win)
    # update display
    pg.display.update()

# main function
def main():
    # create game manger object
    gm = GameManager(WIDTH)
    # create clock object
    clock = pg.time.Clock()
    # runs main loop until set to False
    run = True
    # main loop
    while run:
        # iterate through all events
        for event in pg.event.get():
            # quit event
            if event.type == pg.QUIT:
                run = False
 
        # use clock to set frame rate
        clock.tick(60)  
        # call update window function
        update_win(win, gm)

    # quit pygame		
    pg.quit()	    


# main function call
main()  