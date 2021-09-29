from background import Background
from generation_label import GenerationLabel
from population import Population
from bitcoin import Bitcoin


class Level:

    def __init__(self, width, spawn_pos, btc_pos, pop_size, bg_image_path, fg_image_path):
        self.width = width
        self.bg = Background(width, bg_image_path, fg_image_path) 
        self.gen_label = GenerationLabel()
        self.population = Population(pop_size , spawn_pos)
        self.goal = Bitcoin(btc_pos)

    def update(self, win):
        # show background
        self.bg.show(win)
        # show generation label
        self.gen_label.show(self.population.generation, win, self.width)
        # show goal
        self.goal.show(win)
        # move population
        self.population.update(win, self.width, self.bg.get_image_mask(), self.goal)
        # evolve population
        if self.population.all_dead():
            # calculate fitnesses
            self.population.calculate_fitnesses(self.goal.pos)
            # natural selection
            self.population.natural_selection()
            # mutate new population
            self.population.mutate()
        
