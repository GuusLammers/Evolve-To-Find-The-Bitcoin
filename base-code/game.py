import pygame as pg
from population import Population
from colors import Colors
from goal import Goal


# window dimesions
WIDTH = 750
HEIGHT = WIDTH

# set display caption, width, and height
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Smart Dots')

# colors object
colors = Colors()

# update window function
def update_win(win, population, goal):
    # fill window with black
    win.fill(colors.black())
    # show goal
    goal.show(win)
    # update and show the population
    population.update(WIDTH, HEIGHT, goal.pos)
    population.show(win)
    # check if all dots are dead or have reached the target
    if(population.population_dead()):
        # start genetic algorithm
        # calcualte fitness
        population.calculate_fitnesses(goal.pos)
        # natural selection
        population.natural_selection()
        # mutate
        population.mutate()

    # update display
    pg.display.update()

# main funciton
def main():
    # test
    population = Population(25, (WIDTH/2, WIDTH - 50))
    goal = Goal((WIDTH/2, 50))
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
        update_win(win, population, goal)

    # quit pygame		
    pg.quit()	    


# main function call
main()