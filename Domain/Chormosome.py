from random import randint, choice, random

from Utils import get_communities


class Chromosome:
    def __init__(self, parameters = None, network = None):
        self.__parameters = parameters # parametrii problemei (min,max,
        self.__network = network # matricea adiacenta
        self.__representation = self.__generateCommunities() # reprezentare : vector [nod] = comunitate
        self.__fitness = 0.0
        self.__communities = 0

    def __generateCommunities(self):
        nodes = self.__parameters['nodes']
        matrix = self.__network["mat"]
        communities = [0] * nodes

        contor_nod = 0
        contor_com = 1
        while (contor_nod != nodes):
            rand = randint(0, nodes - 1)

            # daca nodul curent nu apartine de vreo comunitate
            if (communities[rand] == 0):
                communities[rand] = contor_com
                # il bag intr-o comunitate noua si iau toti vecinii nodului si ii bag in comunitatea asta
                for i in range(0, nodes):
                    if (matrix[rand][i] == 1 and communities[i] == 0):
                        communities[i] = contor_com
                        contor_nod += 1
                contor_nod += 1
                contor_com += 1

            # daca avem deja o comunitate, cautam vecinii care nu au asignata o comunitate
            else:
                for i in range(0, nodes):
                    if (matrix[rand][i] == 1 and communities[i] == 0):
                        communities[i] = communities[rand]
                        contor_nod += 1
        return communities

    def crossover(self, otherChromosome):
        # se alege la fiecare nod unul random si se creeaza un cromozom nou
        offspring = []
        for i in range(self.__parameters["nodes"]):
            gene = choice([self.representation[i], otherChromosome.representation[i]])
            offspring.append(gene)
        c = Chromosome(self.__parameters, self.__network)
        c.__representation = offspring
        return c

    def mutation(self):
        # iau o comunitate care deja exista si bag un nod random in ea
        gene = choice(self.__representation)
        pos = randint(0, self.__parameters["nodes"] - 1)
        self.__representation[pos] = gene



    @property
    def representation(self):
        return self.__representation

    @property
    def fitness(self):
        return self.__fitness

    @representation.setter
    def representation(self, c=[]):
        self.__representation = c

    @fitness.setter
    def fitness(self, f=0.0):
        self.__fitness = f

    @property
    def communities(self):
        return get_communities(self.__representation)

    @communities.setter
    def communities(self, com=0):
        self.__communities = com
