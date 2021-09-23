from human import Human
import random

class Population:

    def __init__(self, size, start_position):
        # starting position
        self.start_pos = start_position
        # population of humans
        self.population = [Human(self.start_pos) for _ in range(size)]
        # fitness sum
        self.fitness_sum = 0
        # generation
        self.generation = 0
        # best human
        self.best_human = None
        # fitness sum
        self.fitness_sum = 0

    # update population
    def update(self, win, width, island_mask, goal):
        # iterate through population
        for human in self.population:
            # update human
            human.update(win, width, island_mask, goal) 

    # check if entire population is dead or has reached their goal
    def all_dead(self):
        # iterate through population
        for human in self.population:
            # check if human is alive and hasn't reached their goal
            if not human.dead and not human.reached_goal:
                return False
        # return True if entire population is dead or has reached their goal
        return True        

    # calculate fitnesses
    def calculate_fitnesses(self, goal_pos):
        # iterate through population
        for human in self.population:
            # update dot
            human.calculate_fitness(goal_pos)   

    # natural selection function
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

        # add best human
        self.set_best_human()
        new_population.append(self.get_child(self.best_human, best_human=True))
        # overwrite population with new population
        self.population = new_population
        # increment generation
        self.generation += 1

    # calculate fitness sum
    def sum_fitnesses(self):
        fitness_summation = 0
        # iterate through population
        for human in self.population:
            # add fitness to sum
            fitness_summation += human.fitness
        # set finess_sum
        self.fitness_sum = fitness_summation    

    # select parent 
    def select_parent(self):
        # get random number between 0 and fitness_sum
        rand = random.uniform(0, self.fitness_sum)
        # intantiate sum variable
        sum = 0
        # iterate through population
        for human in self.population:
            # add fitness to sum
            sum += human.fitness
            # check if sum is larger than rand and if it is return dot
            if sum > rand:
                return human 

    # get child
    def get_child(self, parent, best_human=False):
        # set child to be a new dot
        child = Human(self.start_pos, best_human=best_human)         
        # clone parents brain into child
        child.clone(parent)   
        # return child
        return child     

    # set best human of generation
    def set_best_human(self):                          
        index = None
        best_fitness = 0
        # iterate through population
        for i, human in enumerate(self.population):
            # if fitness is better than best_fitness
            if human.fitness > best_fitness:
                # set index and best fitness
                index = i
                best_fitness = human.fitness
        # set best dot
        self.best_human = self.population[index] 

    # mutate
    def mutate(self):
        # iterate through population
        for human in self.population:
            # skip best human
            if human.best:
                continue  
            else:         
                # mutate brain
                human.brain.mutate()         
    