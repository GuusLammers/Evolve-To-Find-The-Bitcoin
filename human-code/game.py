import pygame as pg
from colors import Colors
from population import Population
from bitcoin import Bitcoin
from background import Background
from generation_label import GenerationLabel


# window dimesions
WIDTH = 750
HEIGHT = WIDTH

# set display caption, width, and height
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Human Evolution')

# colors object
colors = Colors()

# update window
def update_win(win, population, goal, background, gen_label):
    # fill window with black
    win.fill(colors.black())

    # show background
    background.show(win)
    # show generation label
    gen_label.show(population.generation, win, WIDTH)
    # show goal
    goal.show(win)
    # move population
    population.update(win, WIDTH, background.get_image_mask(), goal)
    # evolve population
    if population.all_dead():
        # calculate fitnesses
        population.calculate_fitnesses(goal.pos)
        # natural selection
        population.natural_selection()
        # mutate new population
        population.mutate()

    # update display
    pg.display.update()

# main function
def main():
    # create background
    background = Background(WIDTH)
    # create generation label
    gen_label = GenerationLabel()
    # create population
    population = Population(50 , (WIDTH - 150, HEIGHT - 150))
    # create goal
    goal = Bitcoin((100, 100))
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
        update_win(win, population, goal, background, gen_label)

    # quit pygame		
    pg.quit()	    


# main function call
main()  