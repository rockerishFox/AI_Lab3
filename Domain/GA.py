from random import randint
from Domain.Chormosome import Chromosome


class GA:
    def __init__(self, sizePopulation = None, param = None, network = None):
        self.__sizePopulation = sizePopulation
        self.__parameters = param
        self.__network = network
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        # initializam populatia si cream cromozomii
        for _ in range(0, self.__sizePopulation["size"]):
            c = Chromosome(self.__parameters, self.__network)
            self.__population.append(c)

    def evaluation(self):
        # calculam fitness-ul fiecarui cromozom
        for c in self.__population:
            c.fitness = self.__parameters["modularity"](c.representation, self.__parameters, self.__network)

    def best_chromosome(self):
        # alegem cel mai bun cromozom
        crom = self.__population[0]
        for c in self.__population:
            if c.fitness > crom.fitness:
                crom = c
        return crom

    def worst_chromosome(self):
        # alegem cel mai rau cromozom
        crom = self.__population[0]
        for c in self.__population:
            if c.fitness < crom.fitness:
                crom = c
        return crom

    def selection(self):
        # luam doua pozitii random si o luam pe cea mai buna
        pos1 = randint(0, self.__sizePopulation['size'] - 1)
        pos2 = randint(0, self.__sizePopulation['size'] - 1)
        if self.__population[pos1].fitness > self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def evaluate(self, c):
        # calculam fitness-ul fiecarui cromozom
        c.fitness = self.__parameters["modularity"](c.representation, self.__parameters, self.__network)

    def one_generation_elitism(self):
        # facem o noua generatie
        newPop = [self.best_chromosome()]

        for _ in range(self.__sizePopulation['size']):
            # luam 4 cromozomi
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            p3 = self.__population[self.selection()]
            p4 = self.__population[self.selection()]

            # la 2 facem crossover
            off = p1.crossover(p2)
            off2 = p3.crossover(p4)

            # la rezultate facem mutatii
            off.mutation()
            off2.mutation()

            # evaluam rezultatele pentru a obtine fitness-ul fiecaruia
            self.evaluate(off)
            self.evaluate(off2)

            # alegem cromozomul cel mai bun => survival of the fittest
            if off.fitness > off2.fitness:
                newPop.append(off)
            else:
                newPop.append(off2)
        # cromozomul acum are o populatie noua
        self.__population = newPop