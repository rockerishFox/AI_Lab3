from Domain.GA import GA
from repository.Repository import Repository

class Service:
    def __init__(self, fileName):
        self.__repository = Repository(fileName)
        network, [parameters, sizePopulation] = self.__repository.getData()
        self.__ga = GA(sizePopulation, parameters, network)
        self.__ga.initialisation()
        self.__ga.evaluation()
        self.__network = network

    def create_solution(self, generations):
        for gen in range(generations):
            self.__ga.one_generation_elitism()
            best = self.__ga.best_chromosome()
            print (str(gen + 1) + " cu cel mai bun cromozom:\n" + str(best.representation) + "\nCu fitness: " + str(best.fitness) + " si " + str(best.communities) +" comunitati.")

        best = self.__ga.best_chromosome()
        rez = [ best.fitness, best.communities, best.representation, self.__network["mat"]]
        return rez
