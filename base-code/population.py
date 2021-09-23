from dot import Dot
import random

class Population:
    
    def __init__(self, size, start_position):
        # starting position
        self.start_pos = start_position
        # population of dots
        self.population = [Dot(self.start_pos) for _ in range(size)]
        # fitness sum
        self.fitness_sum = 0
        # generation
        self.generation = 0
        # best dot
        self.best_dot = None

    # show population
    def show(self, win):
        # iterate through population
        for dot in self.population:
            # show dot
            dot.show(win)  

    # update population
    def update(self, win_width, win_height, goal_pos):
        # iterate through population
        for dot in self.population:
            # update dot
            dot.update(win_width, win_height, goal_pos) 

    # checks if all dots are dead
    def population_dead(self):
        # iterate through population
        for dot in self.population:
            # check if dot is still alive
            if not dot.dead and not dot.reached_goal:
                return False

        return True                 

    # calculate fitnesses
    def calculate_fitnesses(self, goal_pos):
        # iterate through population
        for dot in self.population:
            # update dot
            dot.calculate_fitness(goal_pos)  

    # natural selection
    def natural_selection(self):
        # instantiate new population
        new_population = []
        # calculate fitness_sum
        self.sum_fitnesses()
        # iterate through length of population
        for _ in range(len(self.population) - 1):
            # get parent
            parent = self.select_parent()
            # add child to new population
            new_population.append(self.get_child(parent))

        # add best dot
        self.set_best_dot()
        new_population.append(self.get_child(self.best_dot, best_dot=True))
        # overwrite population with new population
        self.population = new_population
        # increment generation
        self.generation += 1    

    # mutate
    def mutate(self):
        # iterate through population
        for dot in self.population:
            # skip first dot
            if dot.is_best:
                continue  
            else:         
                # mutate brain
                dot.brain.mutate()

    # calculate fitness sum
    def sum_fitnesses(self):
        fitness_summation = 0
        # iterate through population
        for dot in self.population:
            # add fitness to sum
            fitness_summation += dot.fitness

        # set finess_sum
        self.fitness_sum = fitness_summation    

    # select parent 
    def select_parent(self):
        # get random number between 0 and fitness_sum
        rand = random.uniform(0, self.fitness_sum)
        # intantiate sum variable
        sum = 0
        # iterate through population
        for dot in self.population:
            # add fitness to sum
            sum += dot.fitness
            # check if sum is larger than rand and if it is return dot
            if sum > rand:
                return dot

    # get child
    def get_child(self, parent, best_dot=False):
        # set child to be a new dot
        child = Dot(self.start_pos, best_dot=best_dot)         
        # clone parents brain into child
        child.clone(parent)   
        # return child
        return child

    # set the best dot from previous generation
    def set_best_dot(self):
        index = None
        best_fitness = 0
        # iterate through population
        for i, dot in enumerate(self.population):
            # if fitness is better than best_fitness
            if dot.fitness > best_fitness:
                # set index and best fitness
                index = i
                best_fitness = dot.fitness

        # set best dot
        self.best_dot = self.population[index]         